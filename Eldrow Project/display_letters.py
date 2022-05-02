
from letters import *
def banner_print(word, symbol):
   count = 0
   for row in range(1, 6):
      count=0
      for char in word:
         prlet(char, symbol[count], row)# see prlet.py in letters package
         count +=1
      print() # end of a full row, so print newline
