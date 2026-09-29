# Объявляем список, где все элементы - буквы алфавита.
def get_alphabet():
    return list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')

# Объявляем словарь с текстовыми сообщениями на английском языке.
messages = {
    'choose_letter': 'Choose a letter to make a move.',
    'chose_wrong_letter': "This letter has already been used or it's absent in English alphabet. Try again.",
    'win': 'You win! The ciphered word was: ',
    'lose': 'You lose! The ciphered word was: ',
    'menu': '''You can start a new game or exit. Choose an action:
    1. A new game
    2. Exit'''
}

import random

# Перебираем слова из файла и присваиваем слово переменной word, если оно соответсвует требованиям.
def get_word():
    with open('nouns.txt', 'r', encoding='utf-8') as file:
        nouns = file.read().splitlines()
    while True:
        word = random.choice(nouns).upper().strip()
        if word.isalpha() and 5 <= len(word) <= 10:
            return word