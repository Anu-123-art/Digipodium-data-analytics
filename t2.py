from turtle import *
speed ('fastest')
bgcolor('black')
colors=['pink','green']
i=0

while True:
  pencolor(colors[i%2])
  rt(75)
  fd(300)
  for item in range(5):
    rt(144)
    fd(100)
  i+=1  
mainloop()
       





 
    