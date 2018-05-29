msg="hello world"
print(msg)

# if statement
sd1 = int(input('the first side:'))
sd2 = int(input('the second side:'))
if(sd1 == sd2):
  print("the square's area is", sd1*sd2)
else:
  print("the rectangular's area is", sd1*sd2)

s='python'
for c in s:
  print(c)

for i in range(3,11,2):
  print(i,end=' ')