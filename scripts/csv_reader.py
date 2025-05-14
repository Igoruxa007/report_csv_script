def read_csv(data: list, file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    base_headers = ['id', 'email', 'name', 'department', 'hours_worked', 'hourly_rate']

    headers = lines[0].strip().split(',')
    for i, element in enumerate(headers):
        if element not in base_headers:
            headers[i] = 'hourly_rate'

    for line in lines[1:]:
        values = line.strip().split(',')
        data.append(dict(zip(headers, values)))
