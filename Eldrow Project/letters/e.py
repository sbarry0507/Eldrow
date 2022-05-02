# e.py
# Juliana Gomez, s1321300
# CS-175/501A 03 | DS 502 01
# Spring 2022

# e.py - return one line of 5x5 bannerized letter E
#
#   EEEEE
#   E
#   EEEEE
#   E
#   EEEEE
#

def e(symbol, line):
    s = symbol
    #five strings that for E
    line1 = s * 5
    line2 = s * 1
    line3 = line1
    line4 = line2
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
        return "invalid line"

def main():
    print( e('*', 1) )
    print( e('*', 2) )
    print( e('*', 3) )
    print( e('*', 4) )
    print( e('*', 5) )
if __name__ == '__main__':
    main()
