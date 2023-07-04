from turtle import*
speed('fastest')
for i in range(4):
    pencolor('red')
    fd(100)
    fillcolor('pink')
    begin_fill()
    for i in range(4):
        pencolor('blue')
        fd(100)
        rt(360/4)
    end_fill()    
    lt(360/4)    
            

mainloop()        
