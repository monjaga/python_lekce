import turtle
import math

turtle.shape('turtle')
turtle.color('red', 'brown')


def square():
    turtle.shape('turtle')
    x = 4
    i = 10
    while i < 200:
        while x > 0:
            turtle.forward(i)
            turtle.right(90)
            x -= 1
        else:
            turtle.penup()
            turtle.left(135)
            turtle.forward(14)
            x = 4
            turtle.pendown()
            turtle.right(135)
        i += 20
    turtle.done()


def spider(n):
    turtle.shape('turtle')
    for i in range(0, n * 10, 10):
        turtle.pendown()
        turtle.left(360 / len(range(0, n * 10, 10)))
        turtle.forward(80)
        turtle.stamp()
        turtle.penup()
        turtle.goto(0, 0)
    turtle.done()


def spiral():
    turtle.shape('turtle')
    for i in range(100):
        turtle.circle(i, 50)
    turtle.done()


def square_spiral():
    turtle.shape('turtle')
    sprite = range(0, 200, 2)
    for n in sprite:
        turtle.pendown()
        turtle.left(90)
        turtle.forward(sprite[n])
    turtle.done()


turtle.shape('turtle')
n = 3
r = 15


def more_angles(n, m):
    q = 360 / n
    while n > 0:
        turtle.left(q)
        turtle.forward(m)
        n -= 1


while n < 10:
    m = 2 * r * math.sin(math.pi / n)
    x = (180 - 360 / n) / 2
    turtle.left(x)
    more_angles(n, m)
    turtle.right(x)
    turtle.penup()
    turtle.forward(10)
    turtle.pendown()
    n += 1
    r += 10
