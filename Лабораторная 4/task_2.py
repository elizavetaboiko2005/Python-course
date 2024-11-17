# TODO импортировать необходимые молули
import json
import csv
from csv import DictReader

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME, 'r', newline = '', encoding = 'utf-8') as csv_file:
        reader = DictReader(csv_file) # TODO считать содержимое csv файла
        data_row = [row for row in reader]

    with open(OUTPUT_FILENAME, 'w', encoding = 'utf-8') as json_file:
        json.dump(data_row, json_file, indent = 4)# TODO Сериализовать в файл с отступами равными 4

if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
