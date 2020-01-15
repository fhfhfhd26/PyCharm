import turtle
import random

# 전역변수
sWidth, sHeight, pSize, exitCount = 300, 300, 3, 0
r, g, b, angle, dist, curX, curY = [0]*7

# 메인부분
turtle.title('자유로운 거북이')
turtle.shape('turtle')
turtle.pensize(pSize)
turtle.setup(width=sWidth + 30, height=sHeight + 30)
turtle.screensize(sWidth, sHeight)

while True:
    r = random.random()
    g = random.random()
    b = random.random()
    turtle.pencolor((r, g, b))

    angle = random.randrange(0, 360)
    dist = random.randrange(1, 100)
    turtle.left(angle)
    turtle.forward(dist)
    curX = turtle.xcor()
    curY = turtle.ycor()

    if (((-sWidth / 2) <= curX) and curX <= sWidth / 2) and (((-sHeight / 2) <= curY) and curY <= sHeight / 2):
        pass
    else :
        turtle.penup()
        turtle.goto(0, 0)
        turtle.pendown()

        exitCount += 1
        if exitCount >= 5:
            break

turtle.done()

