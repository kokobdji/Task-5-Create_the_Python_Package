import argparse
import os
from argparse import Namespace

from .collection_framework import (
    counter_unique_characters,
    list_input
)
from .exceptions import NotFound, UnknownFunc


def opening_file(name_file: str) -> list:
    if not os.path.isfile(name_file):
        raise NotFound('File is not exist in directory')
    with open(name_file) as file_rep:
        return [line.rstrip() for line in file_rep]


def parse() -> Namespace:
    parser = argparse.ArgumentParser(
        prog='CollectionFramework',
        description='Takes a string or  text file directory and returns the '
                    'number of unique characters in the string')
    parser.add_argument('--string', default=None, help='enter your string')
    parser.add_argument('--file', default=None, help='enter your file dir')
    args = parser.parse_args()
    if not args.string and not args.file:
        raise UnknownFunc('Must be a file or a string')
    return args


def main(args: Namespace) -> list[int] | int:
    if args.file:
        data = opening_file(args.file)
        return list_input(data)
    return counter_unique_characters(args.string)
