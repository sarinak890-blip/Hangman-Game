import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import lang_ru
import lang_en

def main():
    while True:

        # Определяем функцию для очистки экрана от предыдущих выводов.
        def clear_screen():
            os.system('cls' if os.name == 'nt' else 'clear')

        # Даём игроку выбрать один язык из предложенных двух.
        while True:
            print('''Welcome! Before you start, choose a language:
Добро пожаловать! Перед началом игры выбери язык:
    1: Russian / Русский
    2: English / Английский

            ''')
            choose_language = input().strip()

            # Присваиваем переменной language один из языковых файлов в зависимости от выбранного языка.
            # Проверяем, что было введено именно "1" или "2".
            if choose_language == '1':
                language = lang_ru
                break
            elif choose_language == '2':
                language = lang_en
                break
            else:
                clear_screen()
                print('''
                
                Invalid input! Try again. / Неверный ввод! Попробуй еще раз.
                
                ''')
                continue

        # Вызываем функции из выбранного файла.
        word = language.get_word()
        alphabet = language.get_alphabet()

        # Шифруем загаданное слово.
        ciphered_word = ['_'] * len(word)

        # Определяем функцию, котoрая выводит изображение "виселицы".
        def hangman_image(lives):
            hangman_stages = [
                '            +---+\n            |   |\n            0   |\n           /|\\  |\n           / \\  |\n      +=========|',
                '            +---+\n            |   |\n            0   |\n           /|\\  |\n           /    |\n      +=========|',
                '            +---+\n            |   |\n            0   |\n           /|\\  |\n                |\n      +=========|',
                '            +---+\n            |   |\n            0   |\n           /|   |\n                |\n      +=========|',
                '            +---+\n            |   |\n            0   |\n            |   |\n                |\n      +=========|',
                '            +---+\n            |   |\n            0   |\n                |\n                |\n      +=========|',
                '            +---+\n            |   |\n                |\n                |\n                |\n      +=========|',
                '            +---+\n                |\n                |\n                |\n                |\n      +=========|'
            ]
            return hangman_stages[lives]
        #
        lives = 7

        # Начало одного раунда игры.
        clear_screen()

        #
        while lives > 0 and '_' in ciphered_word:

            # Игровой экран.
            print()
            print(hangman_image(lives))
            print()
            print(*ciphered_word)
            print()
            print(*alphabet)
            print()

            # Выбор буквы из доступных игроку. Проверка на наличие буквы в алфавите.
            while True:
                print(language.messages['choose_letter'])
                print()
                letter = input().upper().strip()
                #
                if letter not in alphabet:
                    print()
                    print(language.messages['chose_wrong_letter'])
                    print()
                else:
                    break

            # Удаление выбранной буквы из алфавита.
            alphabet.remove(letter)

            # Проверка буквы на ее наличие в слове.
            if letter in word:
                for i in range(len(word)):
                    if word[i] == letter:
                        ciphered_word[i] = letter
            else:
                lives -= 1

            # Очищаем экран от предыдущих выводов.
            clear_screen()

            # Проверяем, можно ли окончить игру после этого хода.
            if lives == 0 or "_" not in ciphered_word:
                if lives == 0 and '_' in ciphered_word:
                    print(hangman_image(lives))
                    print()
                    print(language.messages['lose'] + word)
                    print()
                elif '_' not in ciphered_word:
                    print(hangman_image(lives))
                    print()
                    print(language.messages['win'] + word)
                    print()

                # После окончания игры выводим меню с выбором между опциями: начать новую игру или выйти.
                print(language.messages['menu'] + '\n' * 2)
                print()
                while True:
                    menu_choice = input().strip()
                    if menu_choice == '1':
                        clear_screen()
                        break
                    elif menu_choice == '2':
                        clear_screen()
                        print('Спасибо за игру! / Goodbye!')
                        sys.exit()
                    else:
                        continue

if __name__ == "__main__":
    main()