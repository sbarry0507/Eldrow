# b.py - return one line of 5x5 bannerized letter b
#Zak Ahmed

# BBBB
# B   B
# BBBB
# B   B
# BBBB

def b (symbol, line):
    s = symbol
    # five lines that form Z
    line1 = s * 4
    line2 = f'{s}   {s}'
    line3 = line1
    line4 = f'{s}   {s}'
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
    print(b('?',1))
    print(b('X',2))
    print(b('!',3))
    print(b('X',4))
    print(b('X',5))

if __name__ == '__main__':
    main()
