import sys
import os
import string


def get_dir_filepaths(dir_path):
    filepaths = os.listdir(dir_path)
    for file in filepaths:
        filepaths[filepaths.index(file)] = string.join([dir_path,
                                                        '/', file], '')
    return filepaths


def get_file_words_count(*args):
    word_count = {};

    for file in args:
        opened_file = open(file, 'r')

        for line in opened_file:
            for word in string.split(line):
                if word_count.has_key(word):
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        opened_file.close()
    return word_count






