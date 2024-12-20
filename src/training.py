import os
import sys
import yaml
import utils
from logger import Logger
from validator import Validator
from mappings import Mapper

def generate_flags(dict: dict) -> list[str]:
    out = []
    for k, v in dict.items():
        if isinstance(v, bool):
            if v:out.append(f"--{k}")
            continue
        if isinstance(v, str):
            if v == "": continue
        if isinstance(v, list):
            out.append(f"--{k}")
            [out.append(x) for x in v]
            continue
        out.append(f"--{k}={v}")
    return out

def train(arg_dict: dict, sd_scripts_install: str):
    old_work_dir = os.getcwd()
    os.chdir(sd_scripts_install)

    sys.path.append(sd_scripts_install)
    
    #if it's stupid and it works, then it's stupid
    import train_network as tn
    import sdxl_train_network as tn_sdxl
    import library.train_util as train_util
    
    try:
        import lycoris
    except ImportError:
        if arg_dict['network_module'] == 'lycoris.kohya':
            raise ImportError("lycoris.kohya requires lycoris to be installed in your SD-scripts venv")
    sdxl = arg_dict['sdxl']

    if sdxl: 
        lib = tn_sdxl
        trainer = tn_sdxl.SdxlNetworkTrainer()
    else: 
        lib = tn
        trainer = tn.NetworkTrainer()
    logger = Logger(do_info=arg_dict['notify'],do_warn=arg_dict['warnings'])
    
    validator = Validator(logger, arg_dict, arg_dict['handle_errors'])
    validator.validate_all()

    mapper = Mapper(logger,arg_dict)
    mapper.preprocess_config()
    parser = lib.setup_parser()
    flags = generate_flags(arg_dict)
    args = parser.parse_args(flags)
    train_util.verify_command_line_training_args(args)
    args = train_util.read_config_from_file(args, parser)
    print("\n-- Beginning training --")
    trainer.train(args)
    os.chdir(old_work_dir) 
