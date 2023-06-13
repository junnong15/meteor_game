import random
import turtle
import time
import subprocess # import winsound

# 스크린 생성
screen = turtle.Screen()
screen.title("meteor game")
screen.bgcolor("black")
screen.setup(600, 600)
screen.listen() # 키보드 입력을 받을 수 있도록 활성화
turtle.bgpic('galxy.gif')
turtle.addshape("meteorite.gif")

# 초 설정
duration = 30

# 타이머 시작
start_time = time.time()

# 플레이어 생성
player = turtle.Turtle()
player.color("white")
player.penup()
player.speed(10)
player.goto(0, -250)

# 1번 선 함수
def line1():
    line1 = turtle.Turtle()
    line1.color("white")
    line1.penup()
    line1.pensize(5)
    line1.speed(10)
    line1.goto(-100, 300)
    line1.pendown()
    line1.right(90)
    line1.forward(600)

# 2번 선 함수
def line2():
    line2 = turtle.Turtle()
    line2.color("white")
    line2.penup()
    line2.pensize(5)
    line2.speed(10)
    line2.goto(100, 300)
    line2.pendown()
    line2.right(90)
    line2.forward(600)

line1() # 1번 선 생성 실행
line2() # 2번 선 생성 실행



# 개체 왼쪽 움직이기
def move_left():
    player.setx(player.xcor() -200)
    if player.xcor() < -300: # 더 이상 못 가게 이동 제한
        player.goto(-200, -250)
        return

# 개체 오른쪽 움직이기
def move_right():
    player.setx(player.xcor() +200)
    if player.xcor() > 300: # 더 이상 못 가게 이동 제한
        player.goto(200, -250)
        return


# 키보드 입력 활성
screen.listen()
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")

# 소리 재생 정의
def play_sound(filename):
    subprocess.run(["afplay", filename])


# 메테오 생성
x_coordinate = [-200, 0, +200]
meteor = turtle.Turtle()
meteor.shape("meteorite.gif")
meteor.penup()
meteor.speed(10)
meteor.goto(random.choice(x_coordinate), 300)
meteor_speed = 15


# 메테오 떨어지는 속도 램덤
random_speed=int(random.randint(70, 80))

# 이동 횟수 초기화
movement_count = 0

# 최대 음량 설정
max_volume = 70

delay = 1


# 메테오 게임 루프
while True:
    # 타이머 루프 작동
    elapsed_time = time.time() - start_time
    movement_count += 10

    # 최대 음량 설정
    max_volume = 50

    # 볼륨 증가
    volume = (movement_count / 30) * (max_volume / 60)  # 60은 도달 가능한 최대 이동 횟수
    volume = min(volume, max_volume)  # 최대 음량 제한

    # 소리 재생
    subprocess.run(["afplay", "sound_shrotcut_v1.mp3", "-v", str(volume)])
    print(volume)

    # 메테오 아래로 이동
    meteor.sety(meteor.ycor() - random_speed)

    # 메테오 왼쪽 위치 소리 재생
    if meteor.xcor() == -200 and meteor.ycor() < 250 and meteor.ycor() > 200:
        play_sound("left.mp3")

    # 메테오 중앙 위치 소리 재생
    if meteor.xcor() == 0 and meteor.ycor() < 250 and meteor.ycor() > 200:
        play_sound("center.mp3")

    # 메테오 오른쪽 위치 소리 재생
    if meteor.xcor() == 200 and meteor.ycor() < 250 and meteor.ycor() > 200:
        play_sound("right.mp3")

    # 플레이어와 매테오가 치는 경우
    if meteor.distance(player) < 20:
        player.color("red")
        break

    # 메테오가 바닥에 닿았을 경우
    if meteor.ycor() < -300:
        meteor.speed(20)
        meteor.goto(random.choice(x_coordinate), 300)
        max_volume = 0
        movement_count = 0

    # 시간 마감 확인
    if elapsed_time >= duration:
        print("시간 종료")
        break

    # 남은 시간 출력
    remaining_time = duration - elapsed_time
    print(f"남은 시간: {remaining_time:.2f} 초")

    if remaining_time < 15 and remaining_time > 14:
        play_sound("15s_out.mp3")




# 게임 종료
game_over = turtle.Turtle()
game_over.color("white")
game_over.hideturtle()
game_over.write("게임 종료", align="center", font=("Arial", 24, "bold"))
play_sound("game_finsh.mp3")

# 종료
screen.exitonclick()