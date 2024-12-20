import utils
from training import train
from parser import get_parser
import argparse
import os
#TODO:
# - Add a mode to convert a yaml stack to a single yaml modifier file
# - Add a mode to convert a yaml stack into a toml file for direct sd-scripts usage

def main():
    parser = get_parser()
    args = parser.parse_args()
    yaml_list = args.yaml_list
    arg_dict = utils.stack_yamls(yaml_list,'yamls')
    if args.output_to_toml is not None:
        if not os.path.isabs(args.output_to_toml):
            arg_dict['config_file'] = os.path.join(os.getcwd(),args.output_to_toml)
        else:
            arg_dict['config_file'] = args.output_to_toml
        arg_dict['output_config'] = True
    train(arg_dict, args.script_dir)

if __name__ == "__main__":
    main()