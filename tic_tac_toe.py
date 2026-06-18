from turtle import *

screen = Screen()
screen.title("Хрестики-Нулики")
screen.setup(0.9, 0.9)
screen.bgcolor("#E6C4F3")

pen = Turtle()
pen.pensize(4)
pen.speed(0)

turn = ["cross"]
cells = [None, None, None,
        None, None, None,
        None, None, None]
game_over = [False]


def draw_square():
    for i in range(4):
        pen.forward(100)
        pen.left(90)


def draw_line():
    for i in range(3):
        draw_square()
        pen.forward(100)


def draw_field():
    y = 100
    for i in range(3):
        pen.penup()
        pen.goto(-150, y)
        pen.pendown()
        draw_line()
        y -= 100


def draw_x(x, y):
    pen.color("#E9F3C4")
    pen.pensize(5)
    pen.penup()
    pen.goto(x, y)
    pen.pendown()
    pen.goto(x + 100, y + 100)
    pen.penup()
    pen.goto(x, y + 100)
    pen.pendown()
    pen.goto(x + 100, y)
    pen.penup()


def draw_0(x, y):
    pen.color("#C4F3CE")
    pen.pensize(5)
    pen.penup()
    pen.goto(x + 50, y)
    pen.pendown()
    pen.circle(50)
    pen.penup()


def draw_strike(a, b):
    ax = -150 + (a % 3) * 100 + 50
    ay = 100 - (a // 3) * 100 + 50
    bx = -150 + (b % 3) * 100 + 50
    by = 100 - (b // 3) * 100 + 50
    pen.color("#FF2800")
    pen.pensize(6)
    pen.penup()
    pen.goto(ax, ay)
    pen.pendown()
    pen.goto(bx, by)
    pen.penup()


def show_winner(text):
    pen.penup()
    pen.goto(0, 220)
    pen.color("#FF2800")
    pen.write(text, align="center", font=("Arial", 24))


def check():
    if cells[0] == cells[1] == cells[2] and cells[0] != None:
        draw_strike(0, 2)
        show_winner("Победил: " + cells[0])
        game_over[0] = True

    elif cells[3] == cells[4] == cells[5] and cells[3] != None:
        draw_strike(3, 5)
        show_winner("Победил: " + cells[3])
        game_over[0] = True

    elif cells[6] == cells[7] == cells[8] and cells[6] != None:
        draw_strike(6, 8)
        show_winner("Победил: " + cells[6])
        game_over[0] = True

    elif cells[0] == cells[3] == cells[6] and cells[0] != None:
        draw_strike(0, 6)
        show_winner("Победил: " + cells[0])
        game_over[0] = True

    elif cells[1] == cells[4] == cells[7] and cells[1] != None:
        draw_strike(1, 7)
        show_winner("Победил: " + cells[1])
        game_over[0] = True

    elif cells[2] == cells[5] == cells[8] and cells[2] != None:
        draw_strike(2, 8)
        show_winner("Победил: " + cells[2])
        game_over[0] = True

    elif cells[0] == cells[4] == cells[8] and cells[0] != None:
        draw_strike(0, 8)
        show_winner("Победил: " + cells[0])
        game_over[0] = True

    elif cells[2] == cells[4] == cells[6] and cells[2] != None:
        draw_strike(2, 6)
        show_winner("Победил: " + cells[2])
        game_over[0] = True


def is_winner(player):
    if cells[0] == cells[1] == cells[2] == player:
        return True
    elif cells[3] == cells[4] == cells[5] == player:
        return True
    elif cells[6] == cells[7] == cells[8] == player:
        return True
    elif cells[0] == cells[3] == cells[6] == player:
        return True
    elif cells[1] == cells[4] == cells[7] == player:
        return True
    elif cells[2] == cells[5] == cells[8] == player:
        return True
    elif cells[0] == cells[4] == cells[8] == player:
        return True
    elif cells[2] == cells[4] == cells[6] == player:
        return True
    return False


def Proverka():
    for i in range(9):
        if cells[i] is None:
            cells[i] = "zero"
            if is_winner("zero"):
                cells[i] = None
                return i
            cells[i] = None

    for i in range(9):
        if cells[i] is None:
            cells[i] = "cross"
            if is_winner("cross"):
                cells[i] = None
                return i
            cells[i] = None

    for i in range(9):
        if cells[i] is None:
            return i

    return None


def click_mouse(x, y):
    if game_over[0]:
        return

    cell_x = None
    cell_y = None
    index = None

    if x > -150 and x < -50:
        cell_x = -150
        index = 0
    elif x > -50 and x < 50:
        cell_x = -50
        index = 1
    elif x > 50 and x < 150:
        cell_x = 50
        index = 2

    if y < 200 and y > 100:
        cell_y = 100
    elif y < 100 and y > 0:
        cell_y = 0
        index = index + 3
    elif y < 0 and y > -100:
        cell_y = -100
        index = index + 6

    if cell_x != None and cell_y != None:
        if cells[index] == None:

            if turn[0] == "cross":
                draw_x(cell_x, cell_y)
                cells[index] = "cross"
                turn[0] = "zero"
            else:
                draw_0(cell_x, cell_y)
                cells[index] = "zero"
                turn[0] = "cross"

            check()

            filled = True
            for cell in cells:
                if cell == None:
                    filled = False

            if filled and game_over[0] == False:
                show_winner("Ничья")
                game_over[0] = True

            if not game_over[0] and turn[0] == "zero":
                аі = Proverka()
                if аі is not None:
                    cx = -150 + (аі % 3) * 100
                    cy = 100 - (аі // 3) * 100
                    draw_0(cx, cy)
                    cells[аі] = "zero"
                    turn[0] = "cross"
                    check()

                    filled = True
                    for cell in cells:
                        if cell == None:
                            filled = False
                    if filled and game_over[0] == False:
                        show_winner("Ничья")
                        game_over[0] = True


draw_field()
screen.onclick(click_mouse)
mainloop()