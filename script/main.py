from typing import List

from arg_parser import ArgumentParser
from csv_reader import read_csv


def main() -> None:
    argument_parser = ArgumentParser()
    args = argument_parser.parser.parse_args()

    data: List[List[str]] = []
    for file in args.path_to_files:
        read_csv(data, file)
    print(data)


if __name__ == '__main__':
    main()
