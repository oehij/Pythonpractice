def draw_snowman(x, y):
 

    t.up()
    t.goto(x,y+110)
    t.down()
 
    t.begin_fill()
    t.circle(35)
    t.end_fill()
 

    t.up()
    t.goto(x,y+80)
    t.down()
 
    t.lt(20)
    t.fd(90); t.fd(-90)
    t.lt(115)
    t.fd(90); t.fd(-90)
    t.seth(0)
 
    t.begin_fill()
    t.circle(25)
    t.end_fill()
     

    t.up()
    t.goto(x,y)
    t.down()
 
    t.begin_fill()
    t.circle(50)
    t.end_fill()
 
 


import turtle
t = turtle.Turtle()
s = turtle.Screen()
 
t.color('black', 'white')
s.bgcolor('skyblue')
 
for i in range(3):
    draw_snowman(200*i-200,0)