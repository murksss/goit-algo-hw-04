import re
from colorama import Fore, init
init(autoreset=True)


def normalize_phone(phone_number: str) -> str:
    """
    :param phone_number: phone number
    :return: normilized phone number (format: +380XXXXXXXXX)
    """

    # delete all symbols all characters except numbers and '+' from the number.
    normalized_number = re.sub(r'[^\d+]', '', phone_number)
    if len(normalized_number.removeprefix('+38')) == 10:
        if not normalized_number.startswith('+'):
            if not normalized_number.startswith('38'):
                normalized_number = '+38' + normalized_number
            else:
                normalized_number = '+' + normalized_number

        return normalized_number


def bot_answer(msg: str) -> None:
    print(f"{Fore.BLUE}bot: {Fore.CYAN}{msg}")


def add_contact(phone_book: dict[str: str], *args: str) -> None:
    name = args[0]
    phone = normalize_phone(args[1])
    if phone:
        phone_book.update({name: phone})
        bot_answer('Contact added.')
    else:
        bot_answer('Invalid phone number.')


def change_contact(phone_book: dict[str: str], *args: str) -> None:
    name = args[0]
    phone = normalize_phone(args[1])
    if phone:
        phone_book[name] = phone
        bot_answer('Contact updated.')
    else:
        bot_answer('Invalid phone number.')


def show_contact(phone_book: dict[str: str], *args: str) -> None:
    name = args[0]
    if name not in phone_book:
        bot_answer('No contact with that name')
    else:
        bot_answer(f"{name}: {phone_book[name]}")


def show_all(phone_book: dict[str: str]) -> None:
    for key, item in phone_book.items():
        bot_answer(f"{key}: {item}")


def show_info() -> None:
    bot_answer('You can:\n'
               '\t[1] add a new contact: add <name> <phone>\n'
               '\t[2] change a contact: change <name> <new phone>\n'
               '\t[3] get a number: phone <name>\n'
               '\t[4] get all contacts: all\n')
