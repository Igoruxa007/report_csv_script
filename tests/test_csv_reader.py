import tempfile
import os
from scripts.csv_reader import read_csv


def test_read_csv_with_data():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.write("id,email,name,department,hours_worked,hourly_rate\n")
        temp_file.write("1,alice@example.com,Alice Johnson,Marketing,160,50\n")
        temp_file.write("2,bob@example.com,Bob Smith,Design,150,40\n")
        temp_file_path = temp_file.name

    try:
        data = []
        read_csv(data, temp_file_path)

        assert len(data) == 2
        assert data[0] == {
            'id': '1',
            'email': 'alice@example.com',
            'name': 'Alice Johnson',
            'department': 'Marketing',
            'hours_worked': '160',
            'hourly_rate': '50',
        }

        assert data[1] == {
            'id': '2',
            'email': 'bob@example.com',
            'name': 'Bob Smith',
            'department': 'Design',
            'hours_worked': '150',
            'hourly_rate': '40',
        }

    finally:
        os.unlink(temp_file_path)


def test_read_csv_with_salary_column():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.write("id,email,name,department,hours_worked,salary\n")
        temp_file.write("1,alice@example.com,Alice Johnson,Marketing,160,50\n")
        temp_file_path = temp_file.name

    try:
        data = []
        read_csv(data, temp_file_path)
        assert data[0] == {
            'id': '1',
            'email': 'alice@example.com',
            'name': 'Alice Johnson',
            'department': 'Marketing',
            'hours_worked': '160',
            'hourly_rate': '50',
        }

    finally:
        os.unlink(temp_file_path)


def test_read_csv_error_file_not_found(capsys):
    data = []
    read_csv(data, 'file_path')

    captured = capsys.readouterr()

    expected_output = ("Ошибка: файл 'file_path' не найден.\n")

    assert captured.out == expected_output
