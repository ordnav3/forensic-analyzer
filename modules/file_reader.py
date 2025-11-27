import os

def walk_directory(root_path):
    for dirpath, _, filenames in os.walk(root_path):
        for fn in filenames:
            yield os.path.join(dirpath, fn)
