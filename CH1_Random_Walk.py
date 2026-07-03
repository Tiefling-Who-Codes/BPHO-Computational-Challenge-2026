# This program simulates the random walk of particles 
# You can adjust parameters such as number of particles and speed
# Credits: Adrian D'Costa - BPHO Computational Challenge 2026  --- thats me btw :D
# Github: teifling_who_codes/BPHO_comp2026  -- probs the link... havent made it yet :D ... if its not... well... you know who to blame :D

# Imports
import turtle
import math
import random

# Set up the screen
screen = turtle.Screen()

# Initialize the variables
particles = []
colors = ['red', 'blue', 'green', 'yellow', 'orange', 'purple']

############################################################ Get user inputs for the simulation parameters##############################################################################################################

particle_number = turtle.textinput("Particle Number", "Enter the number of particles:")
successful_input = False
while not successful_input:
    try:
        particle_number = int(particle_number)
        if particle_number > 0:
            successful_input = True
        else:
            print("Invalid number of particles. Please enter a positive integer.")
            particle_number = turtle.textinput("Particle Number", "Enter the number of particles:")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        particle_number = turtle.textinput("Particle Number", "Enter the number of particles:")


steps = turtle.textinput("Steps", "Enter the amount of steps for the random walk:")
successful_input = False
while not successful_input:
    try:
        steps = int(steps)
        if steps > 0:
            successful_input = True
        else:
            print("Invalid number of steps. Please enter a positive integer.")
            steps = turtle.textinput("Steps", "Enter the amount of steps for the random walk:")
    except ValueError:
        print("Invalid input. Please enter a positive integer.")
        steps = turtle.textinput("Steps", "Enter the amount of steps for the random walk: ")


speed = turtle.textinput("Speed", "Enter the integer speed of the animation (1-10) Toggle 0 for no movement: ")
successful_input = False
while not successful_input:
    try:
        speed = int(speed)
        if 0 <= speed <= 10:
            successful_input = True
        else:
            print("Invalid speed. Please enter an integer value between 0 and 10.")
            speed = turtle.textinput("Speed", "Enter the integer speed of the animation (1-10) Toggle 0 for no movement: ")
    except ValueError:
        print("Invalid input. Please enter an integer value between 0 and 10.")
        speed = turtle.textinput("Speed", "Enter the integer speed of the animation (1-10) Toggle 0 for no movement: ")
screen.tracer(speed) # Refresh rate of the animation

###########################################################################################################################


# Create the particles
for i in range(particle_number):
    t = turtle.Turtle()
    t.color(random.choice(colors))
    t.speed(speed)
    particles.append(t)

# Move the particles in a random direction -- random walk
for _ in range(steps):
    for particle in particles:
        angle = random.uniform(0, 360) # Random angle in degrees
        distance = random.random() * 20 # Random Distance (Multiples of 20 for better visibility)
        # Move the particle in the random direction
        particle.setheading(angle)
        particle.forward(distance)
    #screen.update()
turtle.done()

#IDK why i have so many comments :D
# Credits to Brown for discovering brownian motion ig... :D
