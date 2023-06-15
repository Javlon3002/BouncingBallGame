import turtle

# set up the screen
screen = turtle.Screen()
screen.title("Simple game")
screen.bgcolor('black')
screen.setup(width=600, height=600)

# set up the  ball
ball = turtle.Turtle()
ball.shape('circle')
ball.color('white')
ball.speed(0)
ball.penup()
ball.goto(0, 200)

x_step = 6
y_step = 4

# set up the bar
bar = turtle.Turtle()
bar.shape('square')
bar.color('white')
bar.shapesize(stretch_wid=1, stretch_len=5)
bar.penup()
bar.goto(0, -280)


# define functions to move the bar
def move_left():
    x = bar.xcor()
    if x > -250:
        x -= 20
    bar.setx(x)


def move_right():
    x = bar.xcor()
    if x < 250:
        x += 20
    bar.setx(x)


screen.listen()
screen.onkeypress(move_left, "Left")
screen.onkeypress(move_right, "Right")

# Main game
while True:
    screen.update()
    ball.setx(ball.xcor() + x_step)
    ball.sety(ball.ycor() + y_step)

    if ball.xcor() > 290 or ball.xcor() < -290:
        x_step *= -1
    if ball.ycor() > 290:
        y_step *= -1

    if (ball.ycor() < -270) and (bar.xcor() - 60 < ball.xcor() < bar.xcor() + 60):
        y_step *= -1

    if ball.ycor() < -300:
        turtle.Screen().bye()
        break

screen.mainloop()
