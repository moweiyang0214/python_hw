# guess number
from random import randint

x=randint(0,300)
print(x)
for count in range(0,5): 
  digit = int(input('please input a number between 0~300:'))
  if digit == x :
    print('bingo')
  elif digit > x:
    print('too large, please try again')
  else:
    print('too small, please try again')