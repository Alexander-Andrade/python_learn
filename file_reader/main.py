import sys


class SkipThisFile(Exception):
    r"""Tells the generator to jump to the next file in list."""
    pass


def read_lines(*file_names):
    for file_name in file_names:
        try:
            with open(file_name) as file:
                for line in file:
                    yield line
        except SkipThisFile:
            yield


def display_files(*files):
    source = read_lines(*files)
    for line in source:
        print(line, end='')
        inp = input()
        if inp == 'n':
            print('NEXT')
            source.throw(SkipThisFile) # return value is ignored


if __name__ == "__main__":
    file_names = sys.argv[1:]
    print(file_names)
    display_files(*file_names)
