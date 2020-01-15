import turtle
import random


# 함수 선언 부분
def screen_left_click(x, y) :
    global r, g, b
    turtle.pencolor((r, g, b))
    turtle.pendown()
    turtle.goto(x,y)


def screen_right_click(x, y) :
    turtle.penup()
    turtle.goto(x, y)


def screen_mid_click(x, y) :
    global r, g, b
    t_size = random.randrange(1, 10)
    turtle.shapesize(t_size)
    r = random.random()
    g = random.random()
    b = random.random()


# 변수 선언 부분
pSize = 10
r, g, b = 0.0, 0.0, 0.0


# 메인 코드 부분
# 실행창 이름 설정
turtle.title("이리온 우쭈쭈")
# 포인터 모양 세팅
turtle.shape("turtle")
# 선의 두께 세팅
turtle.pensize(pSize)

# onscreenclick - 클릭 이벤트 처리
# 왼쪽 버튼 클릭 이벤트 처리 ( , 1)
turtle.onscreenclick(screen_left_click, 1)
# 가운데 버튼 클릭 이벤트 처리 ( , 2)
turtle.onscreenclick(screen_mid_click, 2)
# 오른쪽 버튼 클릭 이벤트 처리 ( , 3)
turtle.onscreenclick(screen_right_click, 3)


turtle.done()

