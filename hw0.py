score = int(input('please input your score:'))
if score>=90 and score <=100 :
  grade = 'A'
elif score>=70 and score <=89 :
  grade = 'B'
elif score >=60 and score <=69 :
  grade = 'C'
elif score >=0 and score <=59:
  grade = 'D'
print('the grade of {} is {}'.format(score, grade))