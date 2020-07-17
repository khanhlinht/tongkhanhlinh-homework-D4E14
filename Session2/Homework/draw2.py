from turtle import *
speed(-1)


for edge in range(3,7):
    if edge%2:
        color('blue')
    else:
        color('red')
    for i in range(edge):
        forward(100)
        left(360/edge)

mainloop()