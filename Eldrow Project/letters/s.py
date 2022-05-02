# Letter s.py
# Rajeev Bhargava, s1331447
# CS-501A 03
# Spring 2022
#   oooo
#  o   
#   ooo 
#      o 
#  oooo
#   
#
def s(symbol, line):
    s = symbol
    # five strings that form s
    line1 = f' {s}{s}{s}{s} '
    line2 = f'{s}'
    line3 = f' {s}{s}{s}'
    line4 = f'    {s}'
    line5 = f'{s}{s}{s}{s} '

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
    print("\n============= s using 'o' letter ==========================\n")
    for i in range(1,6):
        print( s('o', i) )
        
    print("\n============= s using 's' letter ==========================\n")
        
    for i in range(1,6):
        print( s('s', i) )
    
   

if __name__ == '__main__':
    main()
