import csv

from get_names import read_names
from get_initials import format_names
from write_names import write_names
import config


def main():
    names = read_names(config.READ_PATH)
    formated_names = format_names(names)
    sorted_names = sorted(formated_names, key=lambda x: x.split()[-1])
    csv_data = [(i + 1, name) for i, name in enumerate(sorted_names)]
    with open(config.WRITE_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["#", "Инициалы"])
        writer.writerows(csv_data)

    # Задание: писать инициалы отсортированными по алфавиту (по фамилии)
    # Дописать README.md
    # Задание*: писать порядковый номер и в формате csv
    # `*example.csv`


main()