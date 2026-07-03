# This program simulates the random walk of particles and their collisions with a pollen particle. 
# You can adjust parameters such as friction, mass, number of particles, speed, and elasticity to see how they affect the movement of the pollen and particles.
# Credits: Adrian D'Costa - BPHO Computational Challenge 2026
# Github: teifling_who_codes/BPHO_comp2026

# Imports 
import turtle
import math
import random

# Set up the screen and pollen
particles = []
screen = turtle.Screen()
pollen = turtle.Turtle()
pollen.shapesize(3)
pollen.color("brown")
pollen.pendown()
pollen_speed = 0
particle_mass = 1

# Get user inputs for the simulation parameters
friction = turtle.textinput("Friction", "Enter the friction coefficient (0-1) to simulate the slowing down of the pollen over time: ")
successful_input = False
while not successful_input:
    try:
        friction = float(friction)
        if 0 <= friction <= 1:
            successful_input = True
        else:
            print("Invalid friction coefficient. Please enter a value between 0 and 1.")
            friction = turtle.textinput("Friction", "Enter the friction coefficient (0-1) to simulate the slowing down of the pollen over time: ")
    except ValueError:
        print("Invalid input. Please enter a value between 0 and 1.")
        friction = turtle.textinput("Friction", "Enter the friction coefficient (0-1) to simulate the slowing down of the pollen over time: ")

pollen_mass = turtle.textinput("Pollen Mass", "Enter the mass of the pollen relative to the particles: ")
successful_input = False
while not successful_input:
    try:
        pollen_mass = float(pollen_mass)
        if pollen_mass > 0:
            successful_input = True
        else:
            print("Invalid pollen mass. Please enter a positive value.")
            pollen_mass = turtle.textinput("Pollen Mass", "Enter the mass of the pollen relative to the particles: ")
    except ValueError:
        print("Invalid input. Please enter a positive value.")
        pollen_mass = turtle.textinput("Pollen Mass", "Enter the mass of the pollen relative to the particles: ")

particle_number = turtle.textinput("Particle Number", "Enter the number of particles: ")
successful_input = False
while not successful_input:
    try:
        particle_number = int(particle_number)
        if particle_number > 0:
            successful_input = True
        else:
            print("Invalid number of particles. Please enter a positive integer.")
            particle_number = turtle.textinput("Particle Number", "Enter the number of particles: ")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        particle_number = turtle.textinput("Particle Number", "Enter the number of particles: ")

steps = turtle.textinput("Speed", "Enter the speed for the random walk (10-100): ")
successful_input = False
while not successful_input:
    try:
        steps = float(steps)
        if 10 <= steps <= 100:
            successful_input = True
        else:
            print("Invalid steps. Please enter a value between 10 and 100.")
            steps = turtle.textinput("Speed", "Enter the speed for the random walk (10-100): ")
    except ValueError:
        print("Invalid input. Please enter a value between 10 and 100.")
        steps = turtle.textinput("Speed", "Enter the speed for the random walk (10-100): ")

c = turtle.textinput("Elasticity", "Enter the elasticity of the collisions between particles and pollen (0-1): ")
successful_input = False
while not successful_input:
    try:
        c = float(c)
        if 0 <= c <= 1:
            successful_input = True
        else:
            print("Invalid elasticity. Please enter a value between 0 and 1.")
            c = turtle.textinput("Elasticity", "Enter the elasticity of the collisions between particles and pollen (0-1): ")
    except ValueError:
        print("Invalid input. Please enter a value between 0 and 1.")
        c = turtle.textinput("Elasticity", "Enter the elasticity of the collisions between particles and pollen (0-1): ")

speed = turtle.textinput("Speed", "Enter the integer speed of the animation (1-10): ")
successful_input = False
while not successful_input:
    try:
        speed = int(speed)
        if 1 <= speed <= 10:
            successful_input = True
        else:
            print("Invalid speed. Please enter an integer value between 1 and 10.")
            speed = turtle.textinput("Speed", "Enter the integer speed of the animation (1-10): ")
    except ValueError:
        print("Invalid input. Please enter an integer value between 1 and 10.")
        speed = turtle.textinput("Speed", "Enter the integer speed of the animation (1-10): ")

# Refresh rate of the animation
screen.tracer(speed)

# Create the particles
for i in range(particle_number):
    t = turtle.Turtle()
    t.speed(speed)
    particles.append(t)

# Collision logic for the pollen and particles
def move_pollen(heading):
    global pollen_speed
    pollen.setheading(heading) # Move the pollen in the direction of the collision
    #Maths for pollen speed after collision using conservation of momentum and elasticity
    v = (particle_mass * steps + pollen_mass * pollen_speed) / (particle_mass + pollen_mass)
    pollen_speed = c * (v - pollen_speed) + v


while True: # Main simulation loop -- runs forever / until the user closes the window

    for particle in particles:
        # Move the particle in a random direction -- random walk
        particle.penup()
        angle = random.uniform(0, 360)
        distance = random.random() * steps
        particle.setheading(angle)
        particle.forward(distance)

        # Check if the particle is out of bounds and move it back within the screen limits - pacman style
        if particle.xcor() < -screen.window_width() / 2:
            particle.setx(-screen.window_width() / 2)
        elif particle.xcor() > screen.window_width() / 2:
            particle.setx(screen.window_width() / 2)
        if particle.ycor() < -screen.window_height() / 2:
            particle.sety(-screen.window_height() / 2)
        elif particle.ycor() > screen.window_height() / 2:
            particle.sety(screen.window_height() / 2)

        # Check for collision with the pollen
        if particle.distance(pollen) < 25:
            print("Collision detected!")
            particle.setheading(angle + 180)
            v = (particle_mass * steps + pollen_mass * pollen_speed) / (particle_mass + pollen_mass)
            particle_speed = c * (v - steps) + v
            particle.forward(particle_speed)
            move_pollen(angle)


    # Move the pollen based on its current speed and apply friction
    pollen.forward(pollen_speed)
    pollen_speed *= 1 - friction  # Simulate friction to slow down the pollen over time

    # Check if the pollen is out of bounds and move it back within the screen limits - collison style
    if pollen.xcor() < -screen.window_width() / 2:
        pollen.setx(-screen.window_width() / 2)
        pollen_speed = -pollen_speed
    elif pollen.xcor() > screen.window_width() / 2:
        pollen.setx(screen.window_width() / 2)
        pollen_speed = -pollen_speed
    if pollen.ycor() < -screen.window_height() / 2:
        pollen.sety(-screen.window_height() / 2)
        pollen_speed = -pollen_speed
    elif pollen.ycor() > screen.window_height() / 2:
        pollen.sety(screen.window_height() / 2)
        pollen_speed = -pollen_speed

            
# Too tired to add more comments :C 



