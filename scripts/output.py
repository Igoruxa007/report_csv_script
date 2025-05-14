from typing import List, Dict, Tuple


def concole_output(data: List[Dict[str, str]]) -> None:
    headers: List[Tuple[str, str, int]] = [
        ('Department', 'department', 20),
        ('Name', 'name', 20),
        ('Hours', 'hours_worked', 10),
    ]

    header_line = ''.join([f"{header[0]:<{header[2]}}" for header in headers])
    print(header_line)

    department = ''
    for person in data:
        if department != person['department']:
            department = person['department']
            print(department)
        data_line = ''.join([f"{person[element[1]] if element[0] != 'Department' else '' :<{element[2]}}" for element in headers])
        print(data_line)
