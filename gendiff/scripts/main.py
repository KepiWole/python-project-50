#!/usr/bin/env python3

"""A script that runs a main function in terminal."""

from gendiff.generate import generate_diff
import argparse


def parser_function():
    parser = argparse.ArgumentParser(
        description='Compares two configuration files and shows a difference.')
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument('-f',
                        '--format',
                        type=str,
                        default='stylish',
                        help='set format of output')
    args = parser.parse_args()
    return args

def main():
    """A function that creates description in terminal. """
    args = parser_function()
    diff = generate_diff(args.first_file, args.second_file, args.format)
    print(diff)


if __name__ == '__main__':
    main()
