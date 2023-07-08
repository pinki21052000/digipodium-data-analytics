from  turtle import*
#definition

def square(size,color='red'):
    fillcolor(color)
    begin_fill()
    for i in range(4):
     fd(size)
     rt(90)
     end_fill()
     square(100)
     square(50)
     mainloop()

     
