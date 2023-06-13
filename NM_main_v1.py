import turtle
import time
import random
import subprocess


# 거북이 화면 생성 및 설정
screen = turtle.Screen()
screen.title("메테오 게임 (1단계)")
screen.bgcolor("black")
screen.setup(800, 600)
screen.listen() # 키보드 입력을 받을 수 있도록 활성화
open('list.txt', 'w') # 입력 기록 파일 초기화
turtle.addshape("meteorite.gif")
turtle.bgpic('galxy.gif')
turtle.addshape('spaceship.gif')

# 초 설정
duration = 30

# 타이머 시작
start_time = time.time()

# 플레이어 생성
player = turtle.Turtle()
player.shape("spaceship.gif")
player.penup()
player.speed(10)
player.goto(0, -250)


# 플레이어 속도 설정
player_speed = 10

# 개체 왼쪽 움직이기, 개체 왼쪽 입력 텍스트화
def move_left():
    with open('list.txt', "a") as file:
        file.write('a')
    x = player.xcor()
    x -= player_speed
    if x < -380:
        x = -380
    player.setx(x)

# 개체 오른쪽 움직이기, 개체 오른쪽 입력 텍스트화
def move_right():
    with open('list.txt', "a") as file:
        file.write('d')
    x = player.xcor()
    x += player_speed
    if x > 380:
        x = 380
    player.setx(x)

short = 30
max = 60

#메테오1 떨어지는 속도 램덤
random_speed1=int(random.randint(short, max))
#메테오2 떨어지는 속도 램덤
random_speed2=int(random.randint(short, max))
#메테오3 떨어지는 속도 램덤
random_speed3=int(random.randint(short, max))
#메테오4 떨어지는 속도 램덤
random_speed4=int(random.randint(short, max))
#메테오5 떨어지는 속도 램덤
random_speed5=int(random.randint(short, max))
#메테오6 떨어지는 속도 램덤
random_speed6=int(random.randint(short, max))
#메테오7 떨어지는 속도 램덤
random_speed7=int(random.randint(short, max))
#메테오8 떨어지는 속도 램덤
random_speed8=int(random.randint(short, max))
#메테오9 떨어지는 속도 램덤
random_speed9=int(random.randint(short, max))
#메테오10 떨어지는 속도 램덤
random_speed10=int(random.randint(short, max))
#메테오11 떨어지는 속도 램덤
random_speed11=int(random.randint(short, max))
#메테오12 떨어지는 속도 램덤
random_speed12=int(random.randint(short, max))
#메테오13 떨어지는 속도 램덤
random_speed13=int(random.randint(short, max))
#메테오14 떨어지는 속도 램덤
random_speed14=int(random.randint(short, max))
#메테오15 떨어지는 속도 램덤
random_speed15=int(random.randint(short, max))
#메테오16 떨어지는 속도 램덤
random_speed16=int(random.randint(short, max))

# 키보드 입력 그룹
screen.listen()
screen.onkeypress(move_left, "a")
screen.onkeypress(move_right, "d")


# 메테오 생성_1
meteor = turtle.Turtle()
meteor.shape("meteorite.gif")
meteor.penup()
meteor.speed(15)
meteor.goto(random.randint(-380, 0), 310)

# 메테오 생성_2
meteor2 = turtle.Turtle()
meteor2.shape("meteorite.gif")
meteor2.penup()
meteor2.speed(15)
meteor2.goto(random.randint(-380, 0), 310)

# 메테오 생성_3
meteor3 = turtle.Turtle()
meteor3.shape("meteorite.gif")
meteor3.penup()
meteor3.speed(15)
meteor3.goto(random.randint(-380, 0), 310)

# 메테오 생성_4
meteor4 = turtle.Turtle()
meteor4.shape("meteorite.gif")
meteor4.penup()
meteor4.speed(15)
meteor4.goto(random.randint(-380, 0), 310)

# 메테오 생성_5
meteor5 = turtle.Turtle()
meteor5.shape("meteorite.gif")
meteor5.penup()
meteor5.speed(15)
meteor5.goto(random.randint(-380, 0), 310)

# 메테오 생성_6
meteor6 = turtle.Turtle()
meteor6.shape("meteorite.gif")
meteor6.penup()
meteor6.speed(15)
meteor6.goto(random.randint(-380, 0), 310)

# 메테오 생성_7
meteor7 = turtle.Turtle()
meteor7.shape("meteorite.gif")
meteor7.penup()
meteor7.speed(15)
meteor7.goto(random.randint(-380, 0), 310)

# 메테오 생성_8
meteor8 = turtle.Turtle()
meteor8.shape("meteorite.gif")
meteor8.penup()
meteor8.speed(15)
meteor8.goto(random.randint(-380, 0), 310)

# 메테오 생성_9
meteor9 = turtle.Turtle()
meteor9.shape("meteorite.gif")
meteor9.penup()
meteor9.speed(15)
meteor9.goto(random.randint(0, 380), 310)

# 메테오 생성_10
meteor10 = turtle.Turtle()
meteor10.shape("meteorite.gif")
meteor10.penup()
meteor10.speed(15)
meteor10.goto(random.randint(0, 380), 310)

# 메테오 생성_11
meteor11 = turtle.Turtle()
meteor11.shape("meteorite.gif")
meteor11.penup()
meteor11.speed(15)
meteor11.goto(random.randint(0, 380), 310)

# 메테오 생성_12
meteor12 = turtle.Turtle()
meteor12.shape("meteorite.gif")
meteor12.penup()
meteor12.speed(15)
meteor12.goto(random.randint(0, 380), 310)

# 메테오 생성_13
meteor13 = turtle.Turtle()
meteor13.shape("meteorite.gif")
meteor13.penup()
meteor13.speed(15)
meteor13.goto(random.randint(0, 380), 310)

# 메테오 생성_14
meteor14 = turtle.Turtle()
meteor14.shape("meteorite.gif")
meteor14.penup()
meteor14.speed(15)
meteor14.goto(random.randint(0, 380), 310)

# 메테오 생성_15
meteor15 = turtle.Turtle()
meteor15.shape("meteorite.gif")
meteor15.penup()
meteor15.speed(15)
meteor15.goto(random.randint(0, 380), 310)

# 메테오 생성_16
meteor16 = turtle.Turtle()
meteor16.shape("meteorite.gif")
meteor16.penup()
meteor16.speed(15)
meteor16.goto(random.randint(0, 380), 310)


# 라운드2 진입 화면
def goto_round2 ():
    subprocess.call(["python", "goto_round2.py"]) # 일반 모드 게임 진입

def calculate_alphabet_usage(file_path):
    # 탐색 범위 조절
    allowed_letters = {'a', 'd'}

    # 알파벳 개수를 저장할 딕셔너리 생성
    alphabet_count = {letter: 0 for letter in allowed_letters}

    # 텍스트 파일을 읽기 모드로 열기
    with open(file_path, 'r') as file:
        # 파일 내용 읽기
        contents = file.read().lower()

        # 내용의 각 문자에 대해 반복
        for char in contents:
            # 문자가 허용된 알파벳인지 확인
            if char in allowed_letters:
                # 해당 알파벳 개수 증가
                alphabet_count[char] += 1

    # 파일 내 허용된 알파벳의 총 개수 계산
    total_alphabets = sum(alphabet_count.values())

    # 각 알파벳의 사용 비율 계산
    alphabet_percentages = {letter: (count / total_alphabets) * 100 for letter, count in alphabet_count.items()}

    return alphabet_percentages

# 메테오 게임 루프
while True:
    screen.update()

    # 타이머 루프 작동
    elapsed_time = time.time() - start_time

    # 메테오1 아래로 이동
    meteor.sety(meteor.ycor() - random_speed1)

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

    # 메테오13 아래로 이동
    meteor13.sety(meteor13.ycor() - random_speed13)

    # 메테오14 아래로 이동
    meteor14.sety(meteor14.ycor() - random_speed14)

    # 메테오15 아래로 이동
    meteor15.sety(meteor15.ycor() - random_speed15)

    # 메테오16 아래로 이동
    meteor16.sety(meteor16.ycor() - random_speed16)

    # 메테오가 플레이어를 맞았는지에 대한 감지 코드
    if meteor.distance(player) < 20 or meteor2.distance(player) < 20 or meteor3.distance(player) < 20 or meteor4.distance(player) < 20 \
            or meteor5.distance(player) < 20 or meteor6.distance(player) < 20 or meteor7.distance(player) < 20 \
            or meteor8.distance(player) < 20 or meteor9.distance(player) < 20 or meteor10.distance(player) < 20 or meteor11.distance(player) < 20\
            or meteor12.distance(player) < 20 or meteor13.distance(player) < 20 or meteor14.distance(player) < 20 or meteor15.distance(player) < 20\
            or meteor16.distance(player) < 20:

        player.color("red")
        game_over = turtle.Turtle()
        game_over.color("white")
        game_over.hideturtle()
        game_over.write("게임 종료", align="center", font=("Arial", 24, "bold"))
        screen.exitonclick()
        break

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
        meteor7.goto(random.randint(-380, 0), 310)

    # 메테오_8가 지면에 닿을 경우에 대한 코드
    if meteor8.ycor() < -280:
        meteor8.speed(15)
        meteor8.goto(random.randint(-380, 0), 310)

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

    # 메테오_13가 지면에 닿을 경우에 대한 코드
    if meteor13.ycor() < -280:
        meteor13.speed(15)
        meteor13.goto(random.randint(0, 380), 310)

    # 메테오_14가 지면에 닿을 경우에 대한 코드
    if meteor14.ycor() < -280:
        meteor14.speed(15)
        meteor14.goto(random.randint(0, 380), 310)

    # 메테오_15가 지면에 닿을 경우에 대한 코드
    if meteor15.ycor() < -280:
        meteor15.speed(15)
        meteor15.goto(random.randint(0, 380), 310)

    # 메테오_16가 지면에 닿을 경우에 대한 코드
    if meteor16.ycor() < -280:
        meteor16.speed(15)
        meteor16.goto(random.randint(0, 380), 310)

    # 시간 마감 확인
    if elapsed_time >= duration:
        print("게임 종료!, 승리하셨습니다!")
        percentages = calculate_alphabet_usage('list.txt')  # 승리 시 calculate_alphabet_usage 함수 호출
        # 사용자 움직임 비율 출력
        for letter, percentage in percentages.items():
            print(f'{letter}: {percentage}%')
        goto_round2()  # 라운드 2로 선택 화면 진입
        break

    # 남은 시간 출력
    remaining_time = duration - elapsed_time
    print(f"남은 시간: {remaining_time:.2f} 초")

