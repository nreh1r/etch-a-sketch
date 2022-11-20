from turtle import Turtle, Screen

timmy_the_turtle = Turtle()
screen = Screen()


def move_forward():
    timmy_the_turtle.forward(10)


def move_backward():
    timmy_the_turtle.back(10)


def counter_clockwise():
    timmy_the_turtle.left(10)


def clockwise():
    timmy_the_turtle.right(10)


def clear():
    timmy_the_turtle.penup()
    timmy_the_turtle.home()
    timmy_the_turtle.clear()
    timmy_the_turtle.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=counter_clockwise)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
