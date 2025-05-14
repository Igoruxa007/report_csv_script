from scripts.output import console_output


def test_console_output(capsys):
    data = [
        {'department': 'Design', 'name': 'Bob Smith', 'hours_worked': '150'},
        {'department': 'Design', 'name': 'Carol Williams', 'hours_worked': '140'},
        {'department': 'Marketing', 'name': 'Alice Johnson', 'hours_worked': '160'},
    ]

    console_output(data)

    captured = capsys.readouterr()

    expected_output = (
        "Department          Name                Hours     \n"
        "Design\n"
        "                    Bob Smith           150       \n"
        "                    Carol Williams      140       \n"
        "Marketing\n"
        "                    Alice Johnson       160       \n"
    )

    assert captured.out == expected_output
