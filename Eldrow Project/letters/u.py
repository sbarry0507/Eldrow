def u(symbol, line):
    s = symbol
    line1 = f'{s}   {s}'
    line2 = line1
    line3 = line1
    line4 = line1
    line5 = f' {s*3} '

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
    print(u('P', 1))
    print(u('P', 2))
    print(u('P', 3))
    print(u('P', 4))
    print(u('P', 5))


if __name__ == '__main__':
    main()
