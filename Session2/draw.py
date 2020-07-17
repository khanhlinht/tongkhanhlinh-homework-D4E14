from turtle import *
speed(-1)
color('green')
shape('turtle')

for edge in range(3,7):
    for i in range(edge):
        forward(100)
        left(360/edge)

mainloop()