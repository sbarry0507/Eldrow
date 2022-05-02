def w(symbol, line):
    s = symbol
    line1 = f'{s}   {s}'
    line2 = line1
    line3 = f'{s} {s} {s}'
    line4 = f'{s}{s} {s}{s}'
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
    print(w('P', 1))
    print(w('P', 2))
    print(w('P', 3))
    print(w('P', 4))
    print(w('P', 5))


if __name__ == '__main__':
    main()
