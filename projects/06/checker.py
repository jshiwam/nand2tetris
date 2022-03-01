from assembler import Assembler
import argparse

def read_file(filename):
    with open(filename) as f:
        lines = f.readlines()
    return lines

_argparser = argparse.ArgumentParser(description='Compares two *.hack files and return whether they are Equal or Not Equal')
_argparser.add_argument('file1',
metavar='f1',
type=str,
help='first .hack file')

_argparser.add_argument('file2',
metavar='f2',
type=str,
help='second .hack file')

args = _argparser.parse_args()
file1 = args.file1
file2 = args.file2

f1_out = read_file(file1)
f2_out = read_file(file2)

print(f1_out == f2_out)