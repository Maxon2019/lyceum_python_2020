def find_quadratic_equation_roots(a, b, c):
    d = b ** 2 - 4 * a * c
    x1 = (-b + d ** 0.5) / (2 * a)
    x2 = (-b - d ** 0.5) / (2 * a)

    if d == 0:
        return x1
    elif d < 0:
        return None
    else:
        return x1, x2


if __name__ == '__main__':
    a, b, c = map(int, input('Type a,b,c separate with spaces: ').split())
