import turtle

screen = turtle.Screen()

# 1. Draw the track
def draw_track(ax, ay, bx, by):
    
    global track
    track = turtle.Turtle()
    track.hideturtle()
    track.penup()
    track.goto(ax, ay)
    track.pendown()
    track.goto(bx, by)
    global knob
    knob = turtle.Turtle()
    knob.shape("square")
    knob.penup()
    knob.goto((bx-ax)/2 + ax, (by-ay)/2+ay)
    global a1x, a1y, b1x, b1y
    a1x, a1y, b1x, b1y = ax, ay, bx, by


draw_track(-100, 0, 100, 0)


# 3. Handle dragging
def drag_knob(x, y):
    # Lock movement to the X-axis between a1x and b1x
    if a1x <= x <= b1x:
        knob.setx(x)
        # Map X coordinate (a1x to b1x) to a value (0 to 100)
        value = (x - a1x) / (b1x - a1x) * 100
        print(f"Value: {int(value)}")

knob.ondrag(drag_knob)

turtle.done()
