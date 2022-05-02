# n.py - return one line of bannerized letter n
# Antonio Vinagre, s1303334
# CS 175
# Spring 2022
'''
N   N
NN  N
N N N
N  NN
N   N
'''

def n(symbol, line):
    s = symbol
    line1 = f'{s}   {s}'
    line2 = f'{s}{s}  {s}'
    line3 = f'{s} {s} {s}'
    line4 = f'{s}  {s}{s}'
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

    else: #invalid line
        return 'invalid line'

def main():
    print(n('?', 1)) #?   ?
    print(n('X', 2)) #XX  X
    print(n('X', 3)) #X X X
    print(n('X', 4)) #X  XX
    print(n('!', 5)) #!   !
    print(n('@', 6)) #invalid line

if __name__ == '__main__':
    main()
