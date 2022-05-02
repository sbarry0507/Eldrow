def j(symbol, line):
    s = symbol
    line1 = f'  {s*3}'
    line2 = f'    {s}'
    line3 = line2
    line4 = f'{s}   {s}'
    line5 = f' {s * 3} '

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
    print(j('P', 1))
    print(j('P', 2))
    print(j('P', 3))
    print(j('P', 4))
    print(j('P', 5))


if __name__ == '__main__':
    main()
