def read_csv(data: list, file_path: str) -> None:
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    headers = lines[0].strip().split(',')

    for line in lines[1:]:
        values = line.strip().split(',')
        data.append(dict(zip(headers, values)))
