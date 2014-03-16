import sys
import os
import string


def get_dir_filepaths(dir_path):
    filepaths = os.listdir(dir_path)
    for file in filepaths:
        filepaths[filepaths.index(file)] = string.join([dir_path, '/', file], '')
    return filepaths
