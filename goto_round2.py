import turtle
import subprocess

screen = turtle.Screen()
screen.setup(800, 600)

# 좌표 출력 함수
def print_coordinates(x, y):
    print(f"Clicked at coordinates: ({x}, {y})")

def button_click (x, y):
    if x > -50 and x < 50 and y > 20 and y < 60:
        print("2단계 선택")
        # subprocess.call(["python", "NM_main_L2.py"]) # 2단계 게임 진입
        exit()

    elif x > -50 and x < 50 and y > -32 and y < 6:
        print("메인 메뉴 선택")
        subprocess.call(["python", "menu.py"])
        exit()


round2 = turtle.Turtle()
round2.penup()
round2.goto(0, 25)
round2.hideturtle()
round2.write("2단계로", align="center", font=("Arial", 20, "normal"))

goto_menu = turtle.Turtle()
goto_menu.penup()
goto_menu.goto(0, -25)
goto_menu.hideturtle()
goto_menu.write("메인 메뉴로", align="center", font=("Arial", 20, "normal"))

# 화면 클릭 활성화
screen.onclick(button_click)

# 화면 유지
screen.exitonclick()

