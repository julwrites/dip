import os
import yaml


def walk(root, parser):
    levels = [x for x in os.walk(root)]
    for root, dir, files in levels:
        parser(root, dir, files)


def process_dir(root, dirs, files):
    for x in dirs:
        print(abspath, root, x)
    for x in files:
        print(abspath, root, x)


def abspath(root, x):
    return os.path.join(root, x)


def write(file, lines):
    with open(file, "w") as f:
        f.writelines(lines)


def read(file):
    with open(file, "r") as f:
        "\n".join(f.readlines())


def read_config(file):
    yaml.load(read(file), yaml.Loader)
