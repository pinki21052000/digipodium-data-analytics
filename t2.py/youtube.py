from turtle import*
hideturtle()
fillcolor("red")
begin_fill()
for i in range[300, 200] * 2:
    fd(i)
    circle(10,90)
    end_fill()
    penup()
    goto(120,80)
    pendown()
    fillcolor("white")
    begin_fill()
    for i in  [10,120,120]:
        left(i)
        forward(100)
        end_fill()
mainloop()
