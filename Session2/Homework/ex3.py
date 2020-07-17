number = int(input('enter the total number of 1 and 0 '))
for i in range(1, number+1):
    if i % 2 ==1:
        print (1, end=' ')
    else:
        print (0, end=' ')