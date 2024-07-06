import sys
from pathlib import Path
from colorama import Fore, init
init(autoreset=True)

SPACE = "  "


def get_directory_structure(path: Path) -> dict[str: list[dict | str]]:
    """
    :param path: path to folder
    :return: structure like dictionary with list
    """
    directory_structure = dict()
    file_list = list()

    if path.is_dir():
        for entry in path.iterdir():
            if entry.is_file():
                file_list.append(entry.name)
            else:
                file_list.append(get_directory_structure(entry))
        directory_structure[path.name] = file_list

    return directory_structure


def show_directory_structure(directory_structure: dict[str: list[dict | str]], level: int = 0) -> None:
    """
    :param directory_structure: dict with folder structure
    :param level: depth level

    Display the folder structure
    """
    for key, value in directory_structure.items():
        print(f"{SPACE * level}|- {Fore.BLUE}{key}")
        for item in value:
            if type(item) is dict:
                show_directory_structure(item, level + 1)
            else:
                print(f"{SPACE * (level + 1)}|- {Fore.GREEN}{item}")


def main():
    if len(sys.argv) > 1:
        directory_path = Path(sys.argv[1])
        if not directory_path.exists():
            print("Path does not exists")
        elif not directory_path.is_dir():
            print("Path is not a directory")
        else:
            directory_structure = get_directory_structure(directory_path)
            show_directory_structure(directory_structure)
    else:
        print(sys.argv)
        print("Please provide a directory path")


if __name__ == '__main__':
    main()
