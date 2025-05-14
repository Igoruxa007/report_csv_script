from typing import List, Dict

from scripts.arg_parser import ArgumentParser
from scripts.csv_reader import read_csv
from scripts.reports import payout
from scripts.output import concole_output


def main() -> None:
    argument_parser = ArgumentParser()
    args = argument_parser.parser.parse_args()

    data: List[Dict[str, str]] = []

    for file in args.path_to_files:
        read_csv(data, file)

    concole_output(payout(data=data))


if __name__ == '__main__':
    main()
