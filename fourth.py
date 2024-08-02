def parse_input(user_input):
    cmd, *args = user_input.split(' ')
    cmd = cmd.strip().lower()
    return cmd, *args

# decorators

def input_error_add(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter name and phone for the command"
        except KeyError:
            return "We don't have this name in data base, try another"
        except IndexError:
            return "Please try pattern 'add Bob 123456789'"
    return inner

def input_error_change(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter name and phone for the command"
        except KeyError:
            return "We don't have this name in data base, try another"
        except IndexError:
            return "Please try pattern 'change Ross 123456789'"
    return inner

def input_error_phone(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Enter name for the command"
        except KeyError:
            return "We don't have this name in data base, try another"
        except IndexError:
            return "Please try pattern 'phone Dave'"
    return inner

@input_error_add
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error_change
def change_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact updated."

@input_error_phone
def show_phone(args, contacts):
    result = contacts[args[0]]
    return result

def show_all(args, contacts):
    return contacts

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(args, contacts))
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()