#a.py
#Omar Ahmed
#CS175-50
#Spring 2022

#a.py  return  one line of 5X5 banerized letter Z
#Omar Ahmed 

#	 AAA 
#	A   A
#	AAAAA
#	A   A
#	A   A

def a(symbol, line):
    s = symbol
    line1 = f' {s*3} '
    line2 = f'{s}   {s}'
    line3 = s * 5
    line4 = f'{s}   {s}'
    line5 = f'{s}   {s}'

    if line ==1:
        return line1
    if line == 2:
        return line2
    if line ==3:
        return line3
    if line ==4:
        return line4
    if line == 5:
        return line5
    else:
        return "Invalid Line"


def main():
    print(a('!', 1))
    print(a('X' ,2))
    print(a('?', 3))
    print(a('!', 4))
    print(a('X', 5))


if __name__ == '__main__':
    main()
