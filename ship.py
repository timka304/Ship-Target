import pgzrun
import random
import pygame
import itertools

WIDTH = 400
HEIGHT = 400

TITLE = "Ship"

BLOCKPOSITIONS = [(50, 50), (350, 50), (50, 350), (350, 350)]

blockpositions = itertools.cycle(BLOCKPOSITIONS)

block = Actor("block", center = (50, 50))
ship = Actor("ship", center = (WIDTH/2, HEIGHT/2))

def draw():
    screen.clear()
    block.draw()
    ship.draw()

def moveblock():
    animate(block, 'bounce_end', duration = 1, pos = next(blockpositions))

moveblock()

clock.schedule_interval(moveblock, 2)

def nextship():
    x = random.randint(10, 390)
    y = random.randint(10, 390)
    ship.target = x, y
    target_angle = ship.angle_to(ship.target)
    target_angle += 360*((ship.angle-target_angle+180)//360)
    animate(ship, angle = target_angle, duration = 0.3, on_finished = move_ship)

def move_ship():
    animate(ship, tween = 'accel_decel',pos = ship.target, duration = ship.distance_to(ship.target)/200, on_finished = nextship)

nextship()

pgzrun.go()