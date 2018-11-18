import random


def print_omikuji():
    items = ['大吉', '吉', '凶']
    print("今日の運勢は" + random.choice(items) + 'です。')


print_omikuji()
