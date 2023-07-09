from  turtle import*
#definition

def hexagone(size,color='red'):
    fillcolor(color)
    pensize(5)
    pencolor('red')
    begin_fill()
    for i in range(6):
     fd(size)
     rt(72)
     end_fill()
hexagone(100)
def square(size,color='black'):
   fillcolor(color)
   pensize(3)
   pencolor('pink')
   begin_fill()
   for i in range(4):
      fd(size)
      rt(95)
      end_fill()
square(50)
mainloop()







             
   
mainloop()

     
