from pathlib import Path
from colorama import Fore, Style


def total_salary(path: Path = Path('data/employee_salary.txt')) -> tuple[float, float]:
    """
    :param path: path to employee salary file
    :return: sum of salary and mean salary
    """
    with open(path, 'r') as file:
        employee_salary = dict()

        for row in file.read().splitlines():
            name, salary = row.split(',')
            employee_salary[name] = float(salary)

    _sum = sum(employee_salary.values())
    _mean = sum(employee_salary.values())/len(employee_salary)

    return _sum, _mean


if __name__ == '__main__':
    filepath = Path("data/employee_salary.txt")
    try:
        salary_sum, salary_mean = total_salary(filepath)
        print(f"Sum of salary: {Fore.GREEN} {salary_sum} {Style.RESET_ALL}USD")
        print(f"Mean salary: {Fore.GREEN} {salary_mean} {Style.RESET_ALL}USD")
    except FileNotFoundError:
        print(f"Path \"{filepath}\" not found")


