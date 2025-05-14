import tempfile
import os
from scripts.csv_reader import read_csv


def test_read_csv_with_data():
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.write("id,email,name\n")
        temp_file.write("1,alice@example.com,Alice Johnson\n")
        temp_file.write("2,bob@example.com,Bob Smith\n")
        temp_file_path = temp_file.name

    try:
        data = []
        read_csv(data, temp_file_path)

        assert len(data) == 2
        assert data[0] == {'id': '1', 'email': 'alice@example.com', 'name': 'Alice Johnson',}
        assert data[1] == {'id': '2', 'email': 'bob@example.com', 'name': 'Bob Smith',}

    finally:
        os.unlink(temp_file_path)
