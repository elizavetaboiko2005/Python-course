def find_common_participants(str_1, str_2, splitter = ','):
    list_of_participants_1 = str_1.split(splitter)
    list_of_participants_2 = str_2.split(splitter)
    set_of_participants_1 = set(list_of_participants_1)
    set_of_participants_2 = set(list_of_participants_2)
    intersection = set_of_participants_1.intersection(set_of_participants_2)
    sorted_common_intersection = sorted(intersection)
    return sorted_common_intersection

# TODO Напишите функцию find_common_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(f"Общие участники среди двух групп: {find_common_participants(participants_first_group, participants_second_group, splitter = '|')}")
# TODO Провеьте работу функции с разделителем отличным от запятой







