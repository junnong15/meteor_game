import turtle
import math
import random
import time
from NM_main_v1 import calculate_alphabet_usage


# 스크린 생성, 기본 파일 불러오기
screen = turtle.Screen()
screen.title("메테오 게임 (2단계)")
screen.setup(800, 600)
open("list.txt", "r")
turtle.addshape("meteorite.gif")
turtle.bgpic('galxy.gif')
turtle.addshape('spaceship.gif')
turtle.addshape("follow_meteor.gif")

# 플레이어 생성
player = turtle.Turtle()
player.speed(15)
player.penup()
player.shape("spaceship.gif")

# 플레이어 속도 설정
player_speed = 45

# 초 설정
duration = 10

# 타이머 시작
start_time = time.time()

# 플레이어 초기 위치 설정
player.speed(10)
player.penup()
player.goto(0, -250)

# 유도 메테오 생성
follow_meteor = turtle.Turtle()
follow_meteor.shape("follow_meteor.gif")
follow_meteor.speed(1)
follow_meteor.penup()

# 유도 메테오2 생성
follow_meteor2 = turtle.Turtle()
follow_meteor2.shape("follow_meteor.gif")
follow_meteor2.speed(1)
follow_meteor2.penup()

# 유도 메테오3 생성
follow_meteor3 = turtle.Turtle()
follow_meteor3.shape("follow_meteor.gif")
follow_meteor3.speed(1)
follow_meteor3.penup()

# 유도 메테오4 생성
follow_meteor4 = turtle.Turtle()
follow_meteor4.shape("follow_meteor.gif")
follow_meteor4.speed(1)
follow_meteor4.penup()

left_int = 0
right_int = 0
# 일반 메테오 생성_1
meteor = turtle.Turtle()
meteor.shape("meteorite.gif")
meteor.penup()
meteor.speed(15)
meteor.goto(random.randint(-380, left_int), 310)

# 일반 메테오 생성_2
meteor2 = turtle.Turtle()
meteor2.shape("meteorite.gif")
meteor2.penup()
meteor2.speed(15)
meteor2.goto(random.randint(-380, left_int), 310)

# 일반 메테오 생성_3
meteor3 = turtle.Turtle()
meteor3.shape("meteorite.gif")
meteor3.penup()
meteor3.speed(15)
meteor3.goto(random.randint(-380, left_int), 310)

# 일반 메테오 생성_4
meteor4 = turtle.Turtle()
meteor4.shape("meteorite.gif")
meteor4.penup()
meteor4.speed(15)
meteor4.goto(random.randint(-380, left_int), 310)

# 일반 메테오 생성_5
meteor5 = turtle.Turtle()
meteor5.shape("meteorite.gif")
meteor5.penup()
meteor5.speed(15)
meteor5.goto(random.randint(-380, left_int), 310)

# 일반 메테오 생성_6
meteor6 = turtle.Turtle()
meteor6.shape("meteorite.gif")
meteor6.penup()
meteor6.speed(15)
meteor6.goto(random.randint(-380, left_int), 310)

# 일반 메테오 생성_7
meteor7 = turtle.Turtle()
meteor7.shape("meteorite.gif")
meteor7.penup()
meteor7.speed(15)
meteor7.goto(random.randint(right_int, 380), 310)

# 일반 메테오 생성_8
meteor8 = turtle.Turtle()
meteor8.shape("meteorite.gif")
meteor8.penup()
meteor8.speed(15)
meteor8.goto(random.randint(right_int, 380), 310)

# 일반 메테오 생성_9
meteor9 = turtle.Turtle()
meteor9.shape("meteorite.gif")
meteor9.penup()
meteor9.speed(15)
meteor9.goto(random.randint(right_int, 380), 310)

# 일반 메테오 생성_10
meteor10 = turtle.Turtle()
meteor10.shape("meteorite.gif")
meteor10.penup()
meteor10.speed(15)
meteor10.goto(random.randint(right_int, 380), 310)

# 일반 메테오 생성_11
meteor11 = turtle.Turtle()
meteor11.shape("meteorite.gif")
meteor11.penup()
meteor11.speed(15)
meteor11.goto(random.randint(right_int, 380), 310)

# 일반 메테오 생성_12
meteor12 = turtle.Turtle()
meteor12.shape("meteorite.gif")
meteor12.penup()
meteor12.speed(15)
meteor12.goto(random.randint(right_int, 380), 310)

# 유도 메테오의 초기 위치와 방향 설정
follow_meteor.speed(15)
follow_meteor.penup()
follow_meteor.goto(random.randint(-380, 0), 310)
follow_meteor.speed(1)

# 유도 메테오2의 초기 위치와 방향 설정
follow_meteor2.speed(15)
follow_meteor2.penup()
follow_meteor2.goto(random.randint(-380, 0), 310)
follow_meteor2.speed(1)

# 유도 메테오3의 초기 위치와 방향 설정
follow_meteor3.speed(15)
follow_meteor3.penup()
follow_meteor3.goto(random.randint(0, 380), 310)
follow_meteor3.speed(1)

# 유도 메테오4의 초기 위치와 방향 설정
follow_meteor4.speed(15)
follow_meteor4.penup()
follow_meteor4.goto(random.randint(0, 380), 310)
follow_meteor4.speed(1)

# 유도 메테오의 속도 설정
short = 40
max = 60
f_short = 50
f_max = 60
f_random_speed=int(random.randint(f_short, f_max))
f_random_speed2=int(random.randint(f_short, f_max))
f_random_speed3=int(random.randint(f_short, f_max))
f_random_speed4=int(random.randint(f_short, f_max))
random_speed=int(random.randint(short, max))
random_speed2=int(random.randint(short, max))
random_speed3=int(random.randint(short, max))
random_speed4=int(random.randint(short, max))
random_speed5=int(random.randint(short, max))
random_speed6=int(random.randint(short, max))
random_speed7=int(random.randint(short, max))
random_speed8=int(random.randint(short, max))
random_speed9=int(random.randint(short, max))
random_speed10=int(random.randint(short, max))
random_speed11=int(random.randint(short, max))
random_speed12=int(random.randint(short, max))
random_distance=int(random.randint(20, 40))

# 추적자의 움직임 로직 정의
distance = random_distance  # 각 단계에서 전진하는 거리

# 개체 왼쪽 움직이기, 개체 왼쪽 입력 텍스트화
def move_left():
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)

# 개체 오른쪽 움직이기, 개체 오른쪽 입력 텍스트화
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

# 사용자 입력 분석 값 출력
# calculate_alphabet_usage 함수를 사용하여 percentage 값을 계산하고 불러옴
percentages = calculate_alphabet_usage('list.txt')

# 불러온 percentage 값을 사용
a_percentage = percentages['a']
d_percentage = percentages['d']

# a와 d의 차이를 계산
difference = a_percentage - d_percentage

# 중심이 1인 비율을 계산
if difference > 0:
    centered_percentage = 1 + (difference / 100)
elif difference < 0:
    centered_percentage = 1 - abs(difference / 100)
else:
    centered_percentage = 1

# 수정된 비율 출력
print(f"중심이 1인 비율: {centered_percentage}")


while True:
    # 타이머 루프 작동
    elapsed_time = time.time() - start_time

    # 목표의 위치 얻기
    object1_x, object1_y = player.position()

    # 유도 메테오와 플레이어 사이의 각도 계산
    angle = math.degrees(math.atan2(object1_y - follow_meteor.ycor(), object1_x - follow_meteor.xcor()))

    # 유도 메테오2와 플레이어 사이의 각도 계산
    angle2 = math.degrees(math.atan2(object1_y - follow_meteor2.ycor(), object1_x - follow_meteor2.xcor()))

    # 유도 메테오3와 풀레이어 사이의 각도 계산
    angle3 = math.degrees(math.atan2(object1_y - follow_meteor3.ycor(), object1_x - follow_meteor3.xcor()))

    # 유도 메테오4와 풀레이어 사이의 각도 계산
    angle4 = math.degrees(math.atan2(object1_y - follow_meteor4.ycor(), object1_x - follow_meteor4.xcor()))

    # 메테오1 아래로 이동
    meteor.sety(meteor.ycor() - random_speed)

    # 메테오2 아래로 이동
    meteor2.sety(meteor2.ycor() - random_speed2)

    # 메테오3 아래로 이동
    meteor3.sety(meteor3.ycor() - random_speed3)

    # 메테오4 아래로 이동
    meteor4.sety(meteor4.ycor() - random_speed4)

    # 메테오5 아래로 이동
    meteor5.sety(meteor5.ycor() - random_speed5)

    # 메테오6 아래로 이동
    meteor6.sety(meteor6.ycor() - random_speed6)

    # 메테오7 아래로 이동
    meteor7.sety(meteor7.ycor() - random_speed7)

    # 메테오8 아래로 이동
    meteor8.sety(meteor8.ycor() - random_speed8)

    # 메테오9 아래로 이동
    meteor9.sety(meteor9.ycor() - random_speed9)

    # 메테오10 아래로 이동
    meteor10.sety(meteor10.ycor() - random_speed10)

    # 메테오11 아래로 이동
    meteor11.sety(meteor11.ycor() - random_speed11)

    # 메테오12 아래로 이동
    meteor12.sety(meteor12.ycor() - random_speed12)

    # 비율 계산
    target_ratio = centered_percentage # 왼쪽으로 더 가기 위한 비율
    left_ratio = target_ratio - 1
    right_ratio = 1 - target_ratio

    # 좌우 비율에 따른 회전 각도 계산
    left_angle = math.degrees(math.atan(left_ratio))
    right_angle = math.degrees(math.atan(right_ratio))

    # 원하는 움직임에 맞게 각도 조정
    if target_ratio < 1:
        left_angle += 180
        right_angle += 180

    # 유도 메테오 이동
    follow_meteor.speed(f_random_speed)
    follow_meteor.setheading(angle)  # 목표를 향해 회전
    follow_meteor.forward(distance)
    follow_meteor.left(left_angle)
    follow_meteor.right(right_angle)

    if follow_meteor.ycor() < -220:
        follow_meteor.speed(f_random_speed)
        follow_meteor.setheading(270)
        follow_meteor.forward(distance)
        follow_meteor.left(left_angle)
        follow_meteor.right(right_angle)

    # 유도 메테오2 이동
    follow_meteor2.speed(f_random_speed2)
    follow_meteor2.setheading(angle2)  # 목표를 향해 회전
    follow_meteor2.forward(distance)
    follow_meteor2.left(left_angle)
    follow_meteor2.right(right_angle)

    if follow_meteor2.ycor() < -220:
        follow_meteor2.speed(f_random_speed2)
        follow_meteor2.setheading(270)
        follow_meteor2.forward(distance)
        follow_meteor2.left(left_angle)
        follow_meteor2.right(right_angle)

    # 유도 메테오2 이동
    follow_meteor3.speed(f_random_speed3)
    follow_meteor3.setheading(angle3)  # 목표를 향해 회전
    follow_meteor3.forward(distance)
    follow_meteor3.left(left_angle)
    follow_meteor3.right(right_angle)

    if follow_meteor3.ycor() < -220:
        follow_meteor3.speed(f_random_speed4)
        follow_meteor3.setheading(270)
        follow_meteor3.forward(distance)
        follow_meteor3.left(left_angle)
        follow_meteor3.right(right_angle)

    # 유도 메테오2 이동
    follow_meteor4.speed(f_random_speed3)
    follow_meteor4.setheading(angle3)  # 목표를 향해 회전
    follow_meteor4.forward(distance)
    follow_meteor4.left(left_angle)
    follow_meteor4.right(right_angle)

    if follow_meteor4.ycor() < -220:
        follow_meteor4.speed(f_random_speed4)
        follow_meteor4.setheading(270)
        follow_meteor4.forward(distance)
        follow_meteor4.left(left_angle)
        follow_meteor4.right(right_angle)



    # 유도 메테오와 플레이어가 치는 경우
    if follow_meteor.distance(player) < 20 or follow_meteor2.distance(player) < 20 \
            or follow_meteor3.distance(player) < 20 or follow_meteor4.distance(player) < 20 or meteor.distance(player) < 20 or meteor2.distance(player) < 20\
            or meteor3.distance(player) < 20 or meteor4.distance(player) < 20 or meteor5.distance(player) < 20\
            or meteor6.distance(player) < 20 or meteor7.distance(player) < 20 or meteor8.distance(player) < 20 or meteor9.distance(player) < 20\
            or meteor10.distance(player) < 20 or meteor11.distance(player) < 20 or meteor12.distance(player) < 20:
        game_over = turtle.Turtle()
        game_over.color("white")
        game_over.hideturtle()
        game_over.write("게임 패배", align="center", font=("Arial", 24, "bold"))
        break

    # 유도 메테오가 바닥에 닿았을 경우
    if follow_meteor.ycor() < -300:
        follow_meteor.speed(15)
        follow_meteor.goto(random.randint(-380, 0), 310)

    # 유도 메테오2가 바닥에 닿았을 경우
    if follow_meteor2.ycor() < -300:
        follow_meteor2.speed(15)
        follow_meteor2.goto(random.randint(-380, 0), 310)

    # 유도 메테오3가 바닥에 닿았을 경우
    if follow_meteor3.ycor() < -300:
        follow_meteor3.speed(15)
        follow_meteor3.goto(random.randint(0, 380), 310)

    # 유도 메테오4가 바닥에 닿았을 경우
    if follow_meteor4.ycor() < -300:
        follow_meteor4.speed(15)
        follow_meteor4.goto(random.randint(0, 380), 310)

    # 메테오_1가 지면에 닿을 경우에 대한 코드
    if meteor.ycor() < -280:
        meteor.speed(15)
        meteor.goto(random.randint(-380, 0), 310)

    # 메테오_2가 지면에 닿을 경우에 대한 코드
    if meteor2.ycor() < -280:
        meteor2.speed(15)
        meteor2.goto(random.randint(-380, 0), 310)

    # 메테오_3가 지면에 닿을 경우에 대한 코드
    if meteor3.ycor() < -280:
        meteor3.speed(15)
        meteor3.goto(random.randint(-380, 0), 310)

    # 메테오_4가 지면에 닿을 경우에 대한 코드
    if meteor4.ycor() < -280:
        meteor4.speed(15)
        meteor4.goto(random.randint(-380, 0), 310)

    # 메테오_5가 지면에 닿을 경우에 대한 코드
    if meteor5.ycor() < -280:
        meteor5.speed(15)
        meteor5.goto(random.randint(-380, 0), 310)

    # 메테오_6가 지면에 닿을 경우에 대한 코드
    if meteor6.ycor() < -280:
        meteor6.speed(15)
        meteor6.goto(random.randint(-380, 0), 310)

    # 메테오_7가 지면에 닿을 경우에 대한 코드
    if meteor7.ycor() < -280:
        meteor7.speed(15)
        meteor7.goto(random.randint(0, 380), 310)

    # 메테오_8가 지면에 닿을 경우에 대한 코드
    if meteor8.ycor() < -280:
        meteor8.speed(15)
        meteor8.goto(random.randint(0, 380), 310)

    # 메테오_9가 지면에 닿을 경우에 대한 코드
    if meteor9.ycor() < -280:
        meteor9.speed(15)
        meteor9.goto(random.randint(0, 380), 310)

    # 메테오_10가 지면에 닿을 경우에 대한 코드
    if meteor10.ycor() < -280:
        meteor10.speed(15)
        meteor10.goto(random.randint(0, 380), 310)

    # 메테오_11가 지면에 닿을 경우에 대한 코드
    if meteor11.ycor() < -280:
        meteor11.speed(15)
        meteor11.goto(random.randint(0, 380), 310)

    # 메테오_12가 지면에 닿을 경우에 대한 코드
    if meteor12.ycor() < -280:
        meteor12.speed(15)
        meteor12.goto(random.randint(0, 380), 310)

    # 시간 마감 확인
    if elapsed_time >= duration:
        print("게임 종료!, 승리하셨습니다!")
        # 게임 종료
        game_win = turtle.Turtle()
        game_win.color("white")
        game_win.hideturtle()
        game_win.write("게임 승리!", align="center", font=("Arial", 24, "bold"))
        break

# 종료
screen.exitonclick()