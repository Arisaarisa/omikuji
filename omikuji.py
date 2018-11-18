import random


def print_omikuji():
    items = ['大吉', '吉', '凶']
    print(input_name + "の今日の運勢は" + random.choice( items) + 'です。')

input_name =input("名前をおしえてください:")



print_omikuji()
