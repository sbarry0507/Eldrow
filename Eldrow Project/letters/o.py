# o.py - return one line of 5x5 bannerized letter o
# Rajeev Bhargava, s1331447
# CS-501A 03
# Spring 2022
#   ooo
#  o   o
#  o   o 
#  o   o 
#   ooo
#   
#
def o(symbol, line):
    s = symbol
    # five strings that form o
    line1 = f' {s}{s}{s} '
    line2 = f'{s}   {s}'
    line3 = f'{s}   {s}'
    line4 = f'{s}   {s}'
    line5 = f' {s}{s}{s} '

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
        return "invalid line"


def main():
    print( o('X', 1) )
    print( o('X', 2) )
    print( o('X', 3) )
    print( o('X', 4) )
    print( o('X', 5) )

if __name__ == '__main__':
    main()
