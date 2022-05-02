# m.py - return one line of 5x5 bannerized letter M
# Vincent Tuberion
#
#   M   M
#   MM MM
#   M M M
#   M   M
#   M   M
#
def m(symbol, line):
    s = symbol
    # five strings that form Z
    line1 = f'{s}   {s}'
    line2 = f'{s}{s} {s}{s}'
    line3 = f'{s} {s} {s}'
    line4 = f'{s}   {s}'
    line5 = f'{s}   {s}'

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
    print(m('X', 1))
    print(m('X', 2))
    print(m('X', 3))
    print(m('X', 4))
    print(m('X', 5))

if __name__ == '__main__':
    main()
