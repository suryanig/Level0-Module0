import turtle

if __name__ == '__main__':
    window = turtle.Screen()
    window.bgcolor('white')

    # This code makes a new Turtle. Pick a new name for the turtle
    mrgreen = turtle.Turtle()

    # Make your turtle's shape 'turtle', .shape('turtle')
    mrgreen.shape('turtle')
    # Set your turtle's speed using .speed(2)
    mrgreen.speed(2)
    # Set your turtle's color using .color('green') and .pencolor('blue')
    mrgreen.color('green')
    mrgreen.pencolor('blue')
    # Move your turtle forward using .forward(100)
    mrgreen.forward(100)
    # TEST    Did your turtle move forward?

    # Move your turtle left or right using .left(90) or .right(90)
    for i in range(4):
        mrgreen.forward(100)
        mrgreen.right(90)
    # Now put the forward and left/right code into a for loop to repeat 4 times.
    # TEST    Did your turtle draw a square?

    # Move your turtle to a new place on the screen using .goto(x, y)
    # x=0 and y=0 is the center of the screen
    mrgreen.goto(50,50)
    # Have your turtle draw a circle using .circle(radius, steps=30)
    mrgreen.begin_fill()
    mrgreen.circle(17, steps=30)
    mrgreen.end_fill()
    # TEST    Did your turtle draw a circle?

    # Add color to your shape by adding .begin_fill() before drawing the circle
    # and .end_fill() below

    # Draw 3 more shapes with different fill colors!
    mrgreen.color('pink')
    mrgreen.goto(150,70)
    mrgreen.begin_fill()
    for i in range(12):
        mrgreen.forward(70)
        mrgreen.left(30)
    mrgreen.end_fill()

    mrgreen.color('purple')
    mrgreen.goto(-30, -90)
    mrgreen.begin_fill()
    for i in range(3):
        mrgreen.forward(50)
        mrgreen.right(120)
    mrgreen.end_fill()

    mrgreen.color('maroon')
    mrgreen.goto(-1, 78)
    mrgreen.begin_fill()
    for i in range(6):
        mrgreen.forward(20)
        mrgreen.right(60)
    mrgreen.end_fill()
    # ===================== DO NOT EDIT THE CODE BELOW ============================
    turtle.done()
