from turtle import Turtle,Screen

x_posi = [0, -20, -40]
move_dist = 20

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()

    def create_snake(self):
        for turtle_index in range(0, 3):
            t = Turtle("square")
            t.penup()
            t.speed(2)
            t.color("white")
            t.goto(x_posi[turtle_index],0)
            self.turtles.append(t)

    def move(self):
        for turt_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[turt_num - 1].xcor()
            new_y = self.turtles[turt_num - 1].ycor()
            self.turtles[turt_num].goto(new_x, new_y)
        self.turtles[0].forward(move_dist)

    def up(self):
        self.turtles[0].setheading(90)
    def down(self):
        self.turtles[0].setheading(270)
    def left(self):
        self.turtles[0].setheading(180)
    def right(self):
        self.turtles[0].setheading(0)
