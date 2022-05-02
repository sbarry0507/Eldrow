def g(symbol, line):
    s = symbol
    line1 = f' {s * 4}'
    line2 = f'{s}    '
    line3 = f'{s} {s * 3}'
    line4 = f'{s}   {s}'
    line5 = f' {s * 4}'

    if line == 1:
        return line1
    elif line == 2:
        return line2
    elif line == 3:
        return line3
    elif line == 4:
        return line4
    elif line == 5:
        return line5

    else:
        return 'Invalid Line'


def main():
    print(g('P', 1))
    print(g('P', 2))
    print(g('P', 3))
    print(g('P', 4))
    print(g('P', 5))


if __name__ == '__main__':
    main()
