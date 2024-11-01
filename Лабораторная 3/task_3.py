def count_letters(text):
    count = {}
    for char in text:
        if char.isalpha():
            letter = char.lower()
            if letter in count:
                count[letter] += 1
            else:
                count[letter] = 1
    return count


def calculate_frequency(count):
    frequency = {}
    values = count.values()
    total = sum(values)
    items = count.items()
    for char, letter_count in items:
        frequency[char] = letter_count / total
    return frequency# TODO Напишите функцию calculate_frequency


main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""

count = count_letters(main_str)
frequency = calculate_frequency(count)

for letter, letter_frequency in frequency.items():
    print(f"{letter}: {letter_frequency:.2f}")# TODO Распечатайте в столбик букву и её частоту в тексте






