import yaml
import os
import glob
import shutil


def create_dir_safely(dir_path):
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)


def get_sort_dirs(config):
    dirs = []
    for rule in config['rules']:
        dirs.append(os.path.normpath(os.path.join(config['desktop'], rule['name'])))
    return dirs


def normal_glob(pattern):
    pattern = os.path.normpath(pattern)
    return glob.glob(pattern)


def move_files(config):
    sort_dirs = frozenset(get_sort_dirs(config))
    processed_file = set()
    for rule in config['rules']:
        for pattern in rule['patterns']:
            p = os.path.join(config['desktop'], pattern)
            for file in normal_glob(p):
                file = os.path.normpath(file)
                if file not in sort_dirs and file not in processed_file:
                    print("Moving {:} to {:}...".format(file, os.path.join(config['desktop'], rule['name'])))
                    if os.path.exists(os.path.join(config['desktop'], rule['name'], os.path.basename(file))):
                        print("Not moving {:} because doing so will overwrite a sorted file".format(file))
                        processed_file.add(file)
                        continue
                    shutil.move(file, os.path.join(config['desktop'], rule['name']))

def sort_files(config_file):
    with open(config_file, 'r') as fin:
        config = yaml.load(fin)
        config['desktop'] = os.path.expanduser(config['desktop'])

    for dir in get_sort_dirs(config):
        create_dir_safely(dir)

    move_files(config)

if __name__ == '__main__':
    sort_files('../config.yaml')
