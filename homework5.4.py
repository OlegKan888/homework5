def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Enter user name."
        except ValueError:
            return "Give me name and phone please."
        except IndexError:
            return "Invalid input. Please provide the correct arguments."
    return inner

def parse_input(user_input):
    parts = user_input.strip().split(maxsplit=1)
    command = parts[0].lower()  # Команда завжди в нижньому регістрі
    args = parts[1] if len(parts) > 1 else ""  # Аргументи після команди
    return command, args

@input_error
def add_contact(contacts, args):
    parts = args.split()
    if len(parts) != 2:
        raise ValueError()  # Піднімаємо виняток, якщо аргументів не два
    name, phone = parts
    contacts[name] = phone  # Додаємо контакт до словника
    return "Contact added."

@input_error
def change_contact(contacts, args):
    parts = args.split()
    if len(parts) != 2:
        raise ValueError()  # Піднімаємо виняток, якщо аргументів не два
    name, phone = parts
    if name in contacts:
        contacts[name] = phone  # Оновлюємо контакт
        return "Contact updated."
    else:
        raise KeyError()  # Піднімаємо виняток, якщо контакт не знайдено

@input_error
def show_phone(contacts, args):
    name = args.strip()
    if name in contacts:
        return contacts[name]  # Повертаємо номер телефону
    else:
        raise KeyError()  # Піднімаємо виняток, якщо контакт не знайдено

@input_error
def show_all(contacts):
    if not contacts:
        return "No contacts found."
    result = ""
    for name, phone in contacts.items():
        result += f"{name}: {phone}\n"  # Формуємо рядок з контактами
    return result.strip()

def main():                #Основна функція для запуску бота.
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter command: ")
        command, args = parse_input(user_input)

        if command in ('exit', 'close'):
            print("Good bye!")
            break
        elif command == 'hello':
            print("How can I help you?")
        elif command == 'add':
            print(add_contact(contacts, args))
        elif command == 'change':
            print(change_contact(contacts, args))
        elif command == 'phone':
            print(show_phone(contacts, args))
        elif command == 'all':
            print(show_all(contacts))
        else:
            print("Unknown command. Please try again.")

if __name__ == "__main__":
    main()
