from turtle import*
speed('fastest')
bgcolor('black')
colors=['yellow','green','blue','red','purple','orange']
i=0
while True:
    pencolor(colors[i%6])
    fd(10+i)
    lt(200)
    i+=1
mainloop()    
