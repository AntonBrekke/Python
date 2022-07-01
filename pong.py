import turtle
import random as rand


wn = turtle.Screen()
wn.title("Pong Pyhon by Anton Brekke")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("blue")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("red")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,170)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.7
ball.dy = 0.7

# Pen score
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0  Player B: 0", align = 'center', font = ("Bauhaus 93", 24, "normal"))

# Funksjon
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, 'w')

wn.listen()
wn.onkeypress(paddle_a_down, 's')

wn.listen()
wn.onkeypress(paddle_b_up, 'Up')

wn.listen()
wn.onkeypress(paddle_b_down, 'Down')

# Main game loop:
while True:
    wn.update()

    # Bevege ballen
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Grensesjekk
    if ball.ycor() > 290:
        ball.sety(290)
        d = rand.randint(1,3)
        if d == 1:
            d = 0.5
        if d == 2:
            d = 0.3
        if d == 3:
            d = 0.7
        ball.dy = d
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        d = rand.randint(1,3)
        if d == 1:
            d = -0.3
        if d == 2:
            d = -0.4
        if d == 3:
            d = -0.5
        ball.dy = d
        ball.dy *= -1


    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = 'center', font = ("Bauhaus 93", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = 'center', font = ("Bauhaus 93", 24, "normal"))

    # Sprett av paddle
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() - 55:
        ball.setx(340)
        ball.dx *= -1

    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55:
        ball.setx(-340)
        ball.dx *= -1