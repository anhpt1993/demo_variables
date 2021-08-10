import turtle as t

t.pensize(5)

def arc(r,deg):
    t.pendown()
    t.circle(r,180)
    t.penup()
    t.home()
    pass

x = 100
t.penup()
t.goto(0,-x)
t.pendown()
t.fillcolor("yellow")
t.begin_fill()
t.circle(x)
t.end_fill()
t.penup()
t.home()

# vẽ miệng cười
rad_mouth = 70
t.goto(-rad_mouth,0)
t.right(90)
arc(rad_mouth,180)

# vẽ mắt trái
rad_eye = 20
t.goto(-30,30)
t.left(90)
arc(rad_eye,180)

# vẽ mắt phải
t.goto(50,30)
t.left(90)
arc(rad_eye,180)

t.hideturtle()

t.done()
