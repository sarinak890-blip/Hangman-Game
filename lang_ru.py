# Объявляем список, где все элементы - буквы алфавита.
def get_alphabet():
    return list('АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')

# Объявляем словарь с текстовыми сообщениями на русском языке.
messages = {
    'choose_letter': 'Выбери букву, чтобы сделать ход.',
    'chose_wrong_letter': 'Эта буква уже была введена, либо же отсутствует в русском алфавите. Попробуй ещё раз.',
    'win': 'Ура, победа! Загаданное слово: ',
    'lose': 'Не судьба! Загаданное слово: ',
    'menu': '''Ты можешь начать новую игру или выйти. Выбери действие:
    1. Новая игра
    2. Выйти'''
}

import random

# Перебираем слова из файла и присваиваем слово переменной word, если оно соответсвует требованиям.
def get_word():
    with open('russian_nouns.txt', 'r', encoding='utf-8') as file:
        nouns = file.read().splitlines()
    while True:
        word = random.choice(nouns).upper().strip()
        if word.isalpha() and 5 <= len(word) <= 10:
            return word