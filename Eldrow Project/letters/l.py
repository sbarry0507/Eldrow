#l.py
#Kristina Shaw, s1323592
#CS-175
#Spring 2022

#function to establish the string for each line in the letter
def l(symbol, line):
    s = symbol
    line1 = f'{s}   '
    line2 = f'{s}   '
    line3 = f'{s}   '
    line4 = f'{s}   '
    line5 = s * 5

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

#estalishes what symbol will print on each line
def main():
    print( l('*', 1) )
    print( l('*', 2) )
    print( l('*', 3) )
    print( l('*', 4) )
    print( l('*', 5) )
    
#command to run the program if it is valid
if __name__ == '__main__':
    main()
