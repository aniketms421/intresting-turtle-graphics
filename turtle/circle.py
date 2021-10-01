import turtle
turtle.bgcolor("black")
turtle.pensize(1)
turtle.speed(0)

for i in range(6):
    for colors in ['Azure','red', 'magenta', 'blue', 'cyan','green', 'yellow','white','pink','grey']:
        turtle.color(colors)
        turtle.circle(130)
        turtle.left(10)
turtle.hideturtle()