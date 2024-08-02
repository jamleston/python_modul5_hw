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

def filter_logs_by_level(logs: list, level: str) -> str:
    filterFunc = filter(lambda x: level.upper() == x['type'], logs)
    logs_list = list(filterFunc)
    logs_string = ''
    for log in logs_list:
        log_str = str(log['date'] + ' ' + log['time'] + ' ' + log['message'])
        logs_string = logs_string + log_str + '\n'
    return(logs_string)

def count_logs_by_level(logs: list) -> dict:
    count = {'INFO': 0,
             'DEBUG': 0,
             'ERROR': 0,
             'WARNING': 0}
    for log in logs:
        if log['type'] == 'INFO':
            count['INFO'] = count['INFO']+1
        elif log['type'] == 'DEBUG':
            count['DEBUG'] = count['DEBUG']+1
        elif log['type'] == 'ERROR':
            count['ERROR'] = count['ERROR']+1
        elif log['type'] == 'WARNING':
            count['WARNING'] = count['WARNING']+1
    return count

def display_log_counts(counts: dict):
    result = f"Рівень логування | Кількість\n-----------------|----------\nINFO             | {counts['INFO']}\nDEBUG            | {counts['DEBUG']}\nERROR            | {counts['ERROR']}\nWARNING          | {counts['WARNING']}"
    return result

def parse_input(user_input):
    cmd, *args = user_input.split(' ')
    cmd = cmd.strip().lower()
    return cmd, *args

def main():
    print("Welcome to the log-count-programm!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)
        path1 = Path('third//log.txt')
        logs = load_logs(path1)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "all":
            counts = count_logs_by_level(logs)
            result = display_log_counts(counts)
            print(result)
        elif command == "info":
            counts = count_logs_by_level(logs)
            result = display_log_counts(counts)
            print(result)
            specific = filter_logs_by_level(logs, 'info')
            print(specific)
        elif command == "debug":
            counts = count_logs_by_level(logs)
            result = display_log_counts(counts)
            print(result)
            specific = filter_logs_by_level(logs, 'debug')
            print(specific)
        elif command == "error":
            counts = count_logs_by_level(logs)
            result = display_log_counts(counts)
            print(result)
            specific = filter_logs_by_level(logs, 'error')
            print(specific)
        elif command == "warning":
            counts = count_logs_by_level(logs)
            result = display_log_counts(counts)
            print(result)
            specific = filter_logs_by_level(logs, 'warning')
            print(specific)
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()