import turtle
import random

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
ball.dx = 0.5
ball.dy = 0.5

# Ball2
ball2 = turtle.Turtle()
ball2.speed(0)
ball2.shape("circle")
ball2.color("white")
ball2.penup()
ball2.goto(0,0)
ball2.dx = 0.4
ball2.dy = 0.5

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
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)

# Keyboard binding
# Player A
wn.listen()
wn.onkeypress(paddle_a_up, 'w')

wn.listen()
wn.onkeypress(paddle_a_down, 's')


# Player B
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

    ball2.setx(ball2.xcor() - ball2.dx)
    ball2.sety(ball2.ycor() - ball2.dy)

    # Grensesjekk
    # Øvre grense ball
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    # Nedre grense ball
    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
# Linje Player B ball
    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = 'center', font = ("Bauhaus 93", 24, "normal"))
    # Linje Player A ball
    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = 'center', font = ("Bauhaus 93", 24, "normal"))
    # Øvre grense ball2
    if ball2.ycor() > 290:
        ball2.sety(290)
        ball2.dy *= -1
    # Nedre grense ball2
    if ball2.ycor() < -290:
        ball2.sety(-290)
        ball2.dy *= -1
    # Linje Player B ball2
    if ball2.xcor() > 390:
        ball2.goto(0,0)
        ball2.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = 'center', font = ("Bauhaus 93", 24, "normal"))
    # Linje Player A ball2
    if ball2.xcor() < -390:
        ball2.goto(0,0)
        ball2.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align = 'center', font = ("Bauhaus 93", 24, "normal"))

    # Sprett av paddle
    # Paddle Player B ball
    if ball.xcor() > 340 and ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 55 and ball.ycor() > paddle_b.ycor() - 55:
        ball.setx(340)
        ball.dx *= -1
    # Paddle Player A ball
    if ball.xcor() < -340 and ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 55 and ball.ycor() > paddle_a.ycor() - 55:
        ball.setx(-340)
        ball.dx *= -1
    # Paddle Player B ball2
    if ball2.xcor() > 340 and ball2.xcor() < 350 and ball2.ycor() < paddle_b.ycor() + 55 and ball2.ycor() > paddle_b.ycor() - 55:
        ball2.setx(340)
        ball2.dx *= -1
    # Paddle Player A ball2
    if ball2.xcor() < -340 and ball2.xcor() > -350 and ball2.ycor() < paddle_a.ycor() + 55 and ball2.ycor() > paddle_a.ycor() - 55:
        ball2.setx(-340)
        ball2.dx *= -1