from pathlib import Path

def parse_log_line(line: str) -> dict:
    list = line.split()
    dict = {}
    dict['date'] = list[0]
    dict['time'] = list[1]
    dict['type'] = list[2]
    dict['message'] = ' '.join(list[3:])
    return dict

def load_logs(file_path: str) -> list:
    try:
        with open(file_path, "r") as file:
            lines = [el.strip() for el in file.readlines()]
            list_of_logs = []
            for line in lines:
                list_of_logs.append(parse_log_line(line))
            return list_of_logs
    except (TypeError, FileNotFoundError):
        answer = 'path is not correct'
        return(answer)

def filter_logs_by_level(logs: list, level: str) -> list:
    filterFunc = filter(lambda x: level.upper() == x['type'], logs)
    result = list(filterFunc)
    return(result)

path1 = Path('third//log.txt')
a = load_logs(path1)
result = filter_logs_by_level(a, 'info')
print(result)