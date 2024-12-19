import yaml
import os
import re
def read_yaml(path: str) -> dict:
    with open(path, 'r') as f:
        return yaml.safe_load(f)
def write_yaml(path: str, dict: dict) -> None:
    with open(path, 'w') as f:
        yaml.dump(dict, f)
def stack_yamls(paths: list[str],root_dir: str = None) -> dict:
    out = {}
    if root_dir is not None:
        paths = [os.path.join(root_dir,path) for path in paths]
    for path in paths:
        out.update(read_yaml(path))
    return out
def find_training_names(path: str) -> list[str]:
    #training folders are any directory that starts with some number and then an underscore (e.g: 12_folder)
    l = []
    for f in os.listdir(path):
        if re.match(r'^[0-9]+_.*$',f):
            #make sure that it's a folder and not a file
            if os.path.isdir(os.path.join(path,f)):
                l.append(str(re.sub(r'^[0-9]+_','',f)))
    return l