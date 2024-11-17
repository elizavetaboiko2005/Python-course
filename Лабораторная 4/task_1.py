# TODO решите задачу
import json
def task() -> float:
    with open('input.json', 'r') as file:
        data = json.load(file)
    sum = 0

    for item in data:
        if 'score' in item and 'weight' in item:
            multiplication = item['score'] * item['weight']
            sum += multiplication
    return round(sum, 3)
print(task())
