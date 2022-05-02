def y(symbol, line):
    s = symbol
    line1 = f'{s}   {s}'
    line2 = line1
    line3 = f' {s*3} '
    line4 = f'  {s}  '
    line5 = line4

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
    print(y('P', 1))
    print(y('P', 2))
    print(y('P', 3))
    print(y('P', 4))
    print(y('P', 5))


if __name__ == '__main__':
    main()
