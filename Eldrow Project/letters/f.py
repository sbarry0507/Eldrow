#f.py
#Michael Ivanicki, s1321890
#CS-175
#Spring 2022

def f(symbol, line):
    s = symbol
    line1 = s * 5
    line2 = f'{s}'
    line3 = s * 3
    line4 = line2
    line5 = line2

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
    print (f('*',1))
    print (f('*',2))
    print (f('*',3))
    print (f('*',4))
    print (f('*',5))
    
if __name__ == '__main__':
    main()
