def x(symbol, line):
    s = symbol
    line1 = f'{s}   {s}'
    line2 = f' {s} {s} '
    line3 = f'  {s}  '
    line4 = line2
    line5 = line1

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
    print(x('P', 1))
    print(x('P', 2))
    print(x('P', 3))
    print(x('P', 4))
    print(x('P', 5))


if __name__ == '__main__':
    main()
