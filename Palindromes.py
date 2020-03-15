date = input('Введите дату в формате ДД/ММ/ГГГГ: ')
first_dat = date
dat = date.split('/')
date = ''.join(dat)


def palindrome_checker(date):
    if date == date[::-1]:
        return 'Our answer: True'
    else:
        return 'Our answer: False'


print('Is', first_dat, 'a palindrome?', palindrome_checker(date))
