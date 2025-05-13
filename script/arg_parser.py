import argparse


class ArgumentParser:
    def __init__(self) -> None:
        self.parser = argparse.ArgumentParser()
        self._add_arguments()

    def _add_arguments(self) -> None:
        self.parser.add_argument(
            'path_to_files',
            nargs='+',
        )
        self.parser.add_argument('--report', type=str)
