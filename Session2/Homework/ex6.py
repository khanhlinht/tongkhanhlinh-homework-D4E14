for j in range(1,10):
    if j%2:
        for i in range(1,10):
            if i%2:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()
    else:
        for i in range(1,10):
            if i%2:
                print(0, end=' ')
            else:
                print(1, end=' ')
        print()