# z.py - return one line of 5x5 bannerized letter Z
# J. Chung
#
#   ZZZZZ
#      Z
#     Z
#    Z
#   ZZZZZ
#
def z(symbol, line):
    s = symbol
    # five strings that form Z
    line1 = s * 5
    line2 = f'   {s} '
    line3 = f'  {s}  '
    line4 = f' {s}   '
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
    print( z('?', 1) )
    print( z('X', 2) )
    print( z('!', 3) )

if __name__ == '__main__':
    main()
