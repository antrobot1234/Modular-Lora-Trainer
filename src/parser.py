import argparse

def get_parser():
    parser = argparse.ArgumentParser(description='Train a model')
    parser.add_argument('-s','--script_dir', type=str, help='SD scripts directory')
    parser.add_argument('-y','--yaml_list', type=str, nargs='+', help='YAML files to parse')
    parser.add_argument('--output_to_toml', type=str, nargs='?', default=None, help='Output to the given toml file')
    parser.add_argument('--output_to_yaml', type=str, nargs='?', default=None, help='Output the stack the given yaml file')
    return parser