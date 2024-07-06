from pathlib import Path
from colorama import Fore, Style


def get_cats_info(path: Path = Path('../data/cats_info.txt')) -> list[dict[str: str]]:
    """
    :param path: path to file with info about cats
    :return: list of dicts with info about cats
    """
    with open(path, 'r') as file:
        cats_info = list()

        for row in file.read().splitlines():
            tmp_dict = dict()
            _id, name, age = row.split(',')
            tmp_dict['id'] = _id
            tmp_dict['name'] = name
            tmp_dict['age'] = age
            cats_info.append(tmp_dict)

    return cats_info


def get_longest_name(cats_info: list[dict[str: str]]) -> int:
    """
    :param cats_info: list of dicts with info about cats
    :return: the length of the longest name
    """
    name_length = len(cats_info[0]['name'])
    for cat in cats_info[1:]:
        if len(cat['name']) > name_length:
            name_length = len(cat['name'])
    return name_length


def show_cats_info(cats_info: list[dict[str: str]]) -> None:
    """
    :param cats_info: list of dicts with info about cats

    Displays the contents of the list in the console
    """
    space = get_longest_name(cats_info)
    for cat in cats_info:
        print(f'{Fore.RED}id: {Style.RESET_ALL}{cat["id"]:<{space}} | '
              f'{Fore.RED}name: {Style.RESET_ALL}{cat["name"]:<{space}} | '
              f'{Fore.RED}age: {Style.RESET_ALL}{cat["age"]:<2}')


def main():
    filepath = Path('../data/cats_info.txt')
    try:
        cats_info = get_cats_info(filepath)
        show_cats_info(cats_info)

    except FileNotFoundError:
        print(f"Path \"{filepath}\" not found")


if __name__ == '__main__':
    main()
