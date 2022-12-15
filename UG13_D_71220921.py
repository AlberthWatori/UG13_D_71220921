import turtle

t = turtle
t.pencolor("white")
t.bgcolor("purple")

t = turtle
t.penup()
t.goto(-50,50)
t.pendown()

turtle.left(90)
turtle.right(20)
turtle.forward(200)
turtle.right(140)
turtle.forward(200)
turtle.backward(100)
turtle.right(110)
turtle.forward(80)

sc =turtle.screen().exitonclick()
turtle.done()