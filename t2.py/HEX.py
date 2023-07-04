from turtle import *
pencolor('black')
bgcolor("red")
pensize('2')

for i in range(100):
    fd(100 - i)
    rt(60)
    circle(60,270) 
    dot(10, 'pink')
mainloop()