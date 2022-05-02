#Julia Salerno
#CS 175
#Spring 2022
#k.py

# K  K
# K K
# KKKK
# K   K
# K   K

def k(symbol, line):
    s = symbol

    line1= f'{s}  {s} '
    line2= f'{s} {s}  '
    line3= f'{s}{s}{s}{s} '
    line4= f'{s}   {s}'
    line5= f'{s}   {s}'

    if line== 1:
        return line1
    if line== 2:
        return line2
    if line== 3:
        return line3
    if line== 4:
        return line4
    if line== 5:
        return line5
    else:
        return "invalid line"
    
def main():
    print( k('?'), 1)
    print( k('X', 2) )
    print( k('!', 3) )

if __name__ == '__main__':
    main()
