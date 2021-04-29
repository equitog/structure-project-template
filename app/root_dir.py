from os import path


def get_root_dir():
    return path.dirname(path.dirname(path.abspath(__name__)))
