# h.py
# Therese Racancoj
# CS175
# spring


'''
H   H
H   H
HHHHH
H   H
H   H
'''

def h(symbol, line):
    s = symbol
    line1 = f'{s}   {s}'
    line2 = line1
    line3 = s * 5
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
        return 'invalid line'
    
# tast code
def main():

    print( H('H', 1))
    print( H('H', 2))
    print( H('H', 3))
    print( H('H', 4))
    print( H('H', 5))
    print()
    print( H('H', 8))

if __name__ == '__main__':
    main()
