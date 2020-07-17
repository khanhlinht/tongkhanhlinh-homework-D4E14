# age = 20
# print(age>18)
# if age>18:
#     print('khong bi di tu')
# else:
#     print('boc lich mat roi')

# grade = 10
# if grade == 10:
#     print('hoc sinh xuat sac')
# elif grade > 9:
#     print('hoc sinh gioi')
# elif grade > 7:
#     print('hoc sinh kha')
# elif grade > 6:
#     print('hoc sinh trung binh')
# else:
#     print('hoc sinh yeu')


# w = float(input('Your weight is '))
# h = float(input('your height is '))
# bmi = w/(h**2)
# if bmi > 30: 
#     print('very overweight')
# elif bmi > 25:
#     print('overweight')
# elif bmi > 18.5:
#     print('normal')
# else:
#     print('underweight')

# import random
# number = random.randint(0,101)
# print(number)
# if number>60:
#     print('rock&roll')
# elif number>30:
#     print('.-.')
# else:
#     print('T.T')

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
delta = (b**2)-4*a*c
#print(delta)
if delta > 0:
    x1 = -b + (delta**(1/2))/(2*a)
    x2 = -b - (delta**(1/2))/(2*a)
    print('x1 =', x1)
    print('x2 =', x2)
elif delta == 0:
    x1 = -b/(2*a)
    print('x1 = x2 =', x1)
else:
    print('vo nghiem')


