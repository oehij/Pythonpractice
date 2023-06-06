def draw_f():
    for i in range(150):
        t.goto(i,(i**2+1)*0.01)
 
 
#main 
import turtle
t = turtle.Turtle()
t.shape("turtle")

# X선 
t.fd(250)
t.fd(-250)
t.lt(90)
 
# Y선
t.fd(250)
t.fd(-250)
t.rt(90)
 
draw_f()