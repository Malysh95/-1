from get_names import read_names
from get_initials import format_names
from write_names import write_names
import config
import csv

def main():
    names = read_names(config.READ_PATH)
    formated_names = format_names(names)
    sorted_names = sorted(formated_names)
    csv_data = [(i + 1, name) for i, name in enumerate(sorted_names)]
    with open(config.WRITE_PATH, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(["#", "ИНИЦИАЛЫ"])
        writer.writerows(csv_data)

   # Дописать README.md
if __name__ == "__main__":
    main()