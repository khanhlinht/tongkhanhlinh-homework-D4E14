number = int(input('Enter a number: '))
for j in range(1, number+1):
    for i in range(1, number+1):
        a = i*j
        print(a, end='\t')
    print()