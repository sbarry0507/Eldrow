def r(symbol, line):
    s = symbol
    line1 = f'{s*4} '
    line2 = f'{s}   {s}'
    line3 = line1
    line4 = f'{s}  {s} '
    line5 = f'{s}   {s}'

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
    print(r('P', 1))
    print(r('P', 2))
    print(r('P', 3))
    print(r('P', 4))
    print(r('P', 5))


if __name__ == '__main__':
    main()
