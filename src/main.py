import utils
from training import train
from parser import get_parser
import argparse
import os
#TODO:
# - Add a mode to convert a yaml stack to a single yaml modifier file

def output_toml(file_name: str, arg_dict: dict):
    file_name = file_name if file_name.endswith('.toml') else file_name + '.toml'     
    if not os.path.isabs(file_name):
        arg_dict['config_file'] = os.path.join(os.getcwd(),file_name) #if this is not done, it will export into the sd-scripts directory
    else:
        arg_dict['config_file'] = file_name
    arg_dict['output_config'] = True

def output_yaml(file_name: str, arg_dict: dict):
        file_name = file_name if file_name.endswith('.yaml') else file_name + '.yaml'
        out_dict = utils.get_difference(arg_dict,utils.read_yaml(os.path.join('yamls','base.yaml')))
        utils.write_yaml(file_name,out_dict)
        print(f"Config written to {file_name}")
        exit(0)

def main():
    parser = get_parser()
    args = parser.parse_args()
    yaml_list = args.yaml_list
    arg_dict = utils.stack_yamls(yaml_list,'yamls')
    if args.output_to_toml is not None: output_toml(args.output_to_toml, arg_dict)
    if args.output_to_yaml is not None: output_yaml(args.output_to_yaml, arg_dict)
    train(arg_dict, arg_dict['sd-scripts'])

if __name__ == "__main__":
    main()