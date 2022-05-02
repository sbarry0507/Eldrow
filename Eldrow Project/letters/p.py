#Julianna rubinetti
#P.py
#CS-501A
def p(symbol, line):
    s = symbol
    line1 = f'{s * 4}  '
    line2 = f'{s}   {s}'
    line3 = line1
    line4 = f'{s}    '
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
    print(p('P', 1))
    print(p('P', 2))
    print(p('P', 3))
    print(p('P', 4))
    print(p('P', 5))


if __name__ == '__main__':
    main()
