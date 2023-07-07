from turtle import*
def square(size,color='pink'):
    fillcolor(color)
    begin_fill()
    for i in range(4):
        forward(size)
        lt(90)
    end_fill()

def hexagon(size,color):
    fillcolor(color)
    begin_fill()
    for i in range(6):
        forward(size)
        rt(60)
    end_fill()    
square(180,'green')
hexagon(180,'yellow')
square(100)  
hexagon(120,'blue')

mainloop()