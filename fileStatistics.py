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
    word_count = {}

    for file in args:
        opened_file = open(file, 'r')

        for line in opened_file:
            for word in string.split(line):
                if word in word_count:
                    word_count[word] += 1
                else:
                    word_count[word] = 1

        opened_file.close()
    return word_count


def get_file_symbols_count(*args):
    word_symbols_count = {}

    for file in args:
        opened_file = open(file, 'r')

        while True:
            symbol = opened_file.read(1)
            if symbol == "":
                break
            if symbol in word_symbols_count:
                word_symbols_count[symbol] += 1
            else:
                word_symbols_count[symbol] = 1

        opened_file.close()
    return word_symbols_count


def write_dict_to_file(result_file, **kwargs):
    for item in kwargs.items():
            result_file.write("%s = %s\n" % item)


def main():
    if len(sys.argv) == 3:
        file_paths = get_dir_filepaths(sys.argv[1])
        result_file = open(sys.argv[2], 'w')

        result_file.write("Words in all files for directory %s:\n"
                          % sys.argv[1])
        words_in_each_file = get_file_words_count(*file_paths)
        write_dict_to_file(result_file, **words_in_each_file)

        result_file.write("Symbols in all files for directory %s:\n"
                          % sys.argv[1])
        symbols_in_each_file = get_file_symbols_count(*file_paths)
        write_dict_to_file(result_file, **symbols_in_each_file)

        for file in file_paths:
            words_in_file = get_file_words_count(*file)
            symbols_in_file = get_file_symbols_count(*file)
            result_file.write("Statistics for file %s:" % file)

            result_file.write("Words:\n")
            write_dict_to_file(words_in_file)

            result_file.write("Symbols:\n")
            write_dict_to_file(symbols_in_file)

        result_file.close()
    else:
        print("Incorrect number of command line parameters")

if __name__ == "__main__":
    main()