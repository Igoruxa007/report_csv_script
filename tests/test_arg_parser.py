from scripts.arg_parser import ArgumentParser


def test_argument_parser_path_to_files():
    parser = ArgumentParser()
    args = parser.parser.parse_args(['data1.csv', 'data2.csv'])
    assert args.path_to_files == ['data1.csv', 'data2.csv']


def test_argument_parser_report():
    parser = ArgumentParser()
    args = parser.parser.parse_args(['data1.csv', '--report', 'payout'])
    assert args.report == 'payout'


def test_argument_parser_no_report():
    parser = ArgumentParser()
    args = parser.parser.parse_args(['data1.csv', 'data2.csv'])
    assert args.report is None


def test_argument_parser_multiple_files_and_report():
    parser = ArgumentParser()
    args = parser.parser.parse_args(['data1.csv', 'data2.csv', '--report', 'payout'])
    assert args.path_to_files == ['data1.csv', 'data2.csv']
    assert args.report == 'payout'
