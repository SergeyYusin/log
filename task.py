import logging

items = {
   "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
   "зажигалка": 0.1,
    "плед": 0.7,
    "куртка": 0.8,
    "вода": 0.4,
    "блокнот": 0.2
}
max_weight = int(input("Введите вместимость рюкзака: "))
count = 0
backpack = {}

for key, item in items.items():
    count += item
    if max_weight >= count:
        backpack[key] = items[key]
    else:
        count -= item

backpack = {}

for item, weight in items.items():
    if weight <= max_weight:
        backpack[item] = weight
        max_weight -= weight

logging.basicConfig(filename='./log.log', filemode='w', encoding='utf-8', level=logging.INFO, style='{')
logger = logging.getLogger(__name__)
logger.info (msg=f"{backpack}\t - мы положили в рюкзак")
print (f"{sum(backpack.values()) > max_weight}\t - ошибка свободного места больше нет!")
logger.error (msg=f"{sum(backpack.values()) > max_weight}\t - ошибка свободного места больше нет!")
