word = input('Введите любое слово: ')
word_first = word
word = word.upper()


def is_word_a_palindrome(word):
    if word == word[::-1]:
        return 'является палидромом'
    else:
        return 'не является палиндромом'


print('Слово', word_first, is_word_a_palindrome(word))
