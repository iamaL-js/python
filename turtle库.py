import turtle as t

t.speed(10)
t.colormode(255)

#画脸
t.penup()
t.goto(0,-150)
t.pendown()

t.pensize(10)

t.color(255,215,0)
t.begin_fill()
t.circle(150)
t.end_fill()

#左眼绘制
t.penup()
t.goto(-50,50)
t.pendown()

t.pensize(18)
t.pencolor(0,47,167)
t.circle(8)

#右眼绘制
t.penup()
t.goto(50,50)
t.pendown()

t.pensize(18)
t.pencolor(0,47,167)
t.circle(8)

#嘴角绘制
t.penup()
t.goto(-97.5,0)
t.pendown()

t.pensize(18)
t.pencolor(0,47,167)
t.right(90)
t.circle(100,180)

t.done()