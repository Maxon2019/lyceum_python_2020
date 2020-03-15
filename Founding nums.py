str = input()


def num_founder(str):
    str_n =[]
    chars = str.split(' ')
    for char in chars:
        if char.isdigit():
            str_n.append(char)
    return str_n


print(num_founder(str))
