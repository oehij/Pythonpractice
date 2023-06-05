import turtle 
import random 
t=turtle.Turtle() 
    
k=int(input("몇각형을 만들래?"))
l=int(input("길이는 얼마?"))
s=int(input("각도는 얼마?"))
x=0
y=0
c=random.randint(0,3)
def draw(k,c,l,s,x,y): 
    
    for c in ["red","blue","green","yellow"]: #
        x=random.randint(1,200)
        y=random.randint(1,200)
        t.penup()
        t.goto(x,y) 
        t.pendown()
        t.fillcolor(c) 
        t.begin_fill()
        for i in range(k):
             
            t.fd(l)
            t.rt(s)
           
        t.end_fill()    

draw(k,c,l,s,x,y)