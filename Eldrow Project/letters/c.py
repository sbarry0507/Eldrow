def c(symbol, line):
    c = symbol
    line1 = f' {c*4}'
    line2 = f'{c}    '
    line3 = f'{c}    '
    line4 = f'{c}    '
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
        return 'invalid line'

def main():
    print(  c('C', 1) )
    print(  c('C', 2) )
    print(  c('C', 3) )
    print(  c('C', 4) )
    print(  c('C', 1) )

if __name__ == '__main__':
    main()
