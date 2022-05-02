# prlet.py
#
# CS-175/CS-501A/DS-502, Spring 2022

from letters import *

# function prlet - print one line of a letter using one of the letter modules 
#                  in the letters package, followed by a '\t' and no newline
# input1 - the letter to print
# input2 - the character to use to print the letter
# input3 - the line to print
#
def prlet(letter, char, line):
    if letter.lower() == 'a': print(a(char, line), '\t', end='')
    elif letter.lower() == 'b': print(b(char, line), '\t', end='')
    elif letter.lower() == 'c': print(c(char, line), '\t', end='')
    elif letter.lower() == 'd': print(d(char, line), '\t', end='')
    elif letter.lower() == 'e': print(e(char, line), '\t', end='')
    elif letter.lower() == 'f': print(f(char, line), '\t', end='')
    elif letter.lower() == 'g': print(g(char, line), '\t', end='')
    elif letter.lower() == 'h': print(h(char, line), '\t', end='')
    elif letter.lower() == 'i': print(i(char, line), '\t', end='')
    elif letter.lower() == 'j': print(j(char, line), '\t', end='')
    elif letter.lower() == 'k': print(k(char, line), '\t', end='')
    elif letter.lower() == 'l': print(l(char, line), '\t', end='')
    elif letter.lower() == 'm': print(m(char, line), '\t', end='')
    elif letter.lower() == 'n': print(n(char, line), '\t', end='')
    elif letter.lower() == 'o': print(o(char, line), '\t', end='')
    elif letter.lower() == 'p': print(p(char, line), '\t', end='')
    elif letter.lower() == 'q': print(q(char, line), '\t', end='')
    elif letter.lower() == 'r': print(r(char, line), '\t', end='')
    elif letter.lower() == 's': print(s(char, line), '\t', end='')
    elif letter.lower() == 't': print(t(char, line), '\t', end='')
    elif letter.lower() == 'u': print(u(char, line), '\t', end='')
    elif letter.lower() == 'v': print(v(char, line), '\t', end='')
    elif letter.lower() == 'w': print(w(char, line), '\t', end='')
    elif letter.lower() == 'x': print(x(char, line), '\t', end='')
    elif letter.lower() == 'y': print(y(char, line), '\t', end='')
    elif letter.lower() == 'z': print(z(char, line), '\t', end='')
    else: print('error: unknown letter input in prlet')


def main():
    prlet('f', 'F', 1)
    print()


if __name__ == '__main__':
    main()
