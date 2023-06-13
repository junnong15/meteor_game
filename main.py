import turtle
import time
import random
import menu



# 거북이 화면 생성 및 설정
screen = turtle.Screen()
screen.title("Meteor Dodger")
screen.bgcolor("black")
screen.setup(800, 600)

turtle.addshape("meteorite.gif")

# 플레이어 생성
player = turtle.Turtle()
player.color("white")
player.shape("triangle")
player.penup()
player.speed(10)
player.goto(0, -250)

# 플레이어 속도 설정
player_speed = 15

# 개체 왼쪽 움직이기
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)

# 개체 오른쪽 움직이기
def move_right():
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)

# 키보드 입력 그룹
screen.listen()
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# 메테오 생성
meteor = turtle.Turtle()
meteor.color("red")
meteor.shape("meteorite.gif")
meteor.penup()
meteor.goto(random.randint(-380, 380), 250)
meteor_speed =10


# 게임 루프
while True:
    screen.update()

    # Move the meteor down
    meteor.sety(meteor.ycor() - meteor_speed)

    # Check if the meteor hits the player
    if meteor.distance(player) < 20:
        player.color("red")
        break

    # Check if the meteor reaches the bottom
    if meteor.ycor() < -280:
        meteor.speed(10)
        meteor.goto(random.randint(-380, 380), 250)


# 게임 종료
game_over = turtle.Turtle()
game_over.color("white")
game_over.hideturtle()
game_over.write("게임 종료", align="center", font=("Arial", 24, "bold"))

# 종료
screen.exitonclick()

'''
# 타이머 생성
def timer(seconds):

    # 타이머 표시용 거북이 개체 만들기
    timer_turtle = turtle.Turtle()
    timer_turtle.speed(10)
    timer_turtle.penup()
    timer_turtle.goto(-320, 250)  # Adjust the position as needed
    timer_turtle.hideturtle()

    start_time = time.time()
    end_time = start_time + seconds

    while time.time() < end_time:
        remaining_time = int(end_time - time.time())
        timer_turtle.clear()
        timer_turtle.shapesize(100)
        timer_turtle.color("white")
        font_size = 20
        timer_turtle.write("남은 시간: {} 초".format(remaining_time), align="center", font=("Arial", font_size, "normal"))

        #프레임 수 제한
        #time.sleep(0.1)

    timer_turtle.clear()
    timer_turtle.write("게임 끝!")
    timer_turtle.showturtle()

# 시간설정
timer(60)
'''
