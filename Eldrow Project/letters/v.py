def v(symbol, line):
    s = symbol
    line1 = f'{s}   {s}'
    line2 = line1
    line3 = f' {s} {s} '
    line4 = line3
    line5 = f'  {s}  '

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
    print(v('P', 1))
    print(v('P', 2))
    print(v('P', 3))
    print(v('P', 4))
    print(v('P', 5))


if __name__ == '__main__':
    main()
