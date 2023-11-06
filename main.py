
import json
character_1 = {
    "name": "Класс: Кайт-ши.",
    "skills": "Ваши навыки: способность приручать животных.",
    "look": "Ваши внешние особенности: кошачьи уши и хвост."
}
with open("character_1.json", "w") as file:
    json.dump(character_1, file, indent=4)

with open("character_1.json", "r") as file:
    character_1 = json.load(file)
del character_1["name"]

with open("character_1.json", "w") as file:
    json.dump(character_1, file, indent=4)

character_2 = {
    "name": "Класс: Спригган.",
    "skills": "Ваши навыки: универсальны в плане использования вооружения, магия иллюзий, поиск сокровищ.",
    "look": "Ваши внешние особенности: чёрные крылья, имеется броня традиционного черного цвета."
}
with open("character_2.json", "w") as file:
    json.dump(character_2, file, indent=4)

with open("character_2.json", "r") as file:
    character_2 = json.load(file)
del character_2["name"]

with open("character_2.json", "w") as file:
    json.dump(character_2, file, indent=4)

character_3 = {
    "name": "Класс: Саламандр.",
    "skills": "Ваши навыки: высокая сила, магия огня.",
    "look": "Ваши внешние особенности: имеется броня традиционного красного цвета."
}
with open("character_3.json", "w") as file:
    json.dump(character_3, file, indent=4)

with open("character_3.json", "r") as file:
    character_3 = json.load(file)
del character_3["name"]

with open("character_3.json", "w") as file:
    json.dump(character_3, file, indent=4)

character_4 = {
    "name": "Класс: Сильфид.",
    "skills": "Ваши навыки: магия ветра, магия исцеления.",
    "look": "Ваши внешние особенности: зеленые крылья и глаза, чаще всего желтые или зеленые волосы."
}
with open("character_4.json", "w") as file:
    json.dump(character_4, file, indent=4)

with open("character_4.json", "r") as file:
    character_4 = json.load(file)
del character_4["name"]

with open("character_4.json", "w") as file:
    json.dump(character_4, file, indent=4)

character_5 = {
    "name": "Класс: Ундин.",
    "skills": "Ваши навыки: магия воды, магия исцеления.",
    "look": "Ваши внешние особенности: синие волосы."
}
with open("character_5.json", "w") as file:
    json.dump(character_5, file, indent=4)

with open("character_5.json", "r") as file:
    character_5 = json.load(file)
del character_5["name"]

with open("character_5.json", "w") as file:
    json.dump(character_5, file, indent=4)


import csv
character1 = [
    ["Кайт-ши."],
    ["Ваши навыки: способность приручать животных."],
    ["Ваши внешние особенности: кошачьи уши и хвост."]
 ]
with open('character1.csv', 'w', newline="") as file:
    writer = csv.writer(file)
    for row in character1:
        writer.writerow(row)

character2 = [
    ["Класс: Спригган."],
    ["Ваши навыки: универсальны в плане использования вооружения, магия иллюзий, поиск сокровищ."],
    ["Ваши внешние особенности: чёрные крылья, имеется броня традиционного черного цвета."]
]
with open('character2.csv', 'w', newline="") as file:
    writer = csv.writer(file)
    for row in character2:
        writer.writerow(row)

character3 = [
    ["Класс: Саламандр."],
    ["Ваши навыки: высокая сила, магия огня."],
    ["Ваши внешние особенности: имеется броня традиционного красного цвета."]
]
with open('character3.csv', 'w', newline="") as file:
    writer = csv.writer(file)
    for row in character3:
        writer.writerow(row)

character4 = [
    ["Класс: Сильфид."],
    ["Ваши навыки: магия ветра, магия исцеления."],
    ["Ваши внешние особенности: зеленые крылья и глаза, чаще всего желтые или зеленые волосы."]
]
with open('character4.csv', 'w', newline="") as file:
    writer = csv.writer(file)
    for row in character4:
        writer.writerow(row)

character5 = [
    ["Класс: Ундин."],
    ["Ваши навыки: магия воды, магия исцеления."],
    ["Ваши внешние особенности: синие волосы."]
]
with open('character5.csv', 'w', newline="") as file:
    writer = csv.writer(file)
    for row in character5:
        writer.writerow(row)