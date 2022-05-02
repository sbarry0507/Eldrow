# Stephen Barry

def q(symbol, line):
    s = symbol
    line1 = f' {s}{s}  '
    line2 = f'{s}  {s} '
    line3 = line2
    line4 = line2
    line5 = f' {s}{s}{s}{s}'

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
    print(q('Q', 1))
    print(q('Q', 2))
    print(q('Q', 3))
    print(q('Q', 4))
    print(q('Q', 5))


if __name__ == '__main__':
    main()
