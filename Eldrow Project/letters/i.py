def i(symbol, line):
    s = symbol
    line1 = f'  {s}  '
    line2 = line1
    line3 = line1
    line4 = line1
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
    print(i('P', 1))
    print(i('P', 2))
    print(i('P', 3))
    print(i('P', 4))
    print(i('P', 5))


if __name__ == '__main__':
    main()
