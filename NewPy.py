import math
import sys
import random
import pygame
import time
from pygame.locals import K_ESCAPE, KEYDOWN, QUIT, K_LSHIFT, MOUSEBUTTONDOWN, K_SPACE
from datetime import datetime


pygame.init()

movement_speed = 5
WIDTH = 800
HEIGHT = 600
SIZE = (WIDTH, HEIGHT)

screen = pygame.display.set_mode(SIZE)
clock = pygame.time.Clock()

# ---------------------------
# Initialize global variables

cloud_x_1 = 100
cloud_y_1 = 50
cloud_x_2 = 300
cloud_y_2 = 80
cloud_x_3 = 530
cloud_y_3 = 110
circle_x = 200
circle_y = 200
orbit_origin_x = (WIDTH/2)
orbit_origin_y = HEIGHT
sun_x = 700
sun_y = 300
angle_sun = 180
angle_moon = 0
building_x = 450
building_y = 165
current_time = datetime.now()
cloud_colour = (230, 230, 230)
cloud1size = random.randint(25,35)

# ---------------------------

running = True
while running:
#     EVENT HANDLING
#     for event in pygame.event.get():
#         if event.type == KEYDOWN:
#             if event.key == K_ESCAPE:
#                 running = False
#         elif event.type == QUIT:
#             running = False
         elif event.type == MOUSEBUTTONDOWN:
             print (pygame.mouse.get_pos())

#     GAME STATE UPDATES
    if angle_sun > 185 and angle_sun < 355:
        day = True
    else:
        day = False

    
    
    # All game math and comparisons happen here
    
    if angle_sun >= 360:
        angle_sun = 0
    theta_sun = math.radians(angle_sun)
    sun_x = orbit_origin_x + math.cos(theta_sun)*(WIDTH*(3/4))
    sun_y = orbit_origin_y + math.sin(theta_sun)*(HEIGHT*(3/4))
    angle_sun += 1

    if angle_moon >= 360:
        angle_moon = 0
    theta_moon = math.radians(angle_moon)
    moon_x = orbit_origin_x + math.cos(theta_moon)*(WIDTH*(3/4))
    moon_y = orbit_origin_y + math.sin(theta_moon)*(HEIGHT*(3/4))
    angle_moon += 1
    
    if cloud_x_1 > -200:
        cloud_x_1 -= random.randint(3,4)
    else:
        cloud_x_1 = WIDTH + 50
        cloud_y_1 = random.randint(30, HEIGHT - 360)
    
    if cloud_x_2 > -200:
        cloud_x_2 -= random.randint(2,3)
    else:
        cloud_x_2 = WIDTH + 50
        cloud_y_2 = random.randint(30, HEIGHT - 360)

    if cloud_x_3 > -200:
        cloud_x_3 -= random.randint(1,2)
    else:
        cloud_x_3 = WIDTH + 50
        cloud_y_3 = random.randint(30, HEIGHT - 360)

    # DRAWING
    if angle_sun > 185 and angle_sun < 355:
        time_colour = (120, 175, 210)
    elif angle_sun <= 185 and angle_sun > 180:
        time_colour = (210, 102, 0)
    elif angle_sun >= 355 and angle_sun < 360:
        time_colour = (65, 85, 125)
    else:
        time_colour = (25, 25, 35)

    screen.fill(time_colour)  # always the first drawing command

    if day == True:
        window_colour = (45, 170, 245)
    else:
        window_colour = (221,105,0)
    
    window_sill = (70, 70, 70)
    dark_wood_colour = (130, 93, 33)
    light_wood_colour = (155, 116, 56)
    
    print(angle_sun)

    pygame.draw.circle(screen, (253, 184, 19), (sun_x, sun_y), 40)
    pygame.draw.circle(screen, (210, 210, 210), (moon_x, moon_y), 40)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_1, cloud_y_1), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_1 + 40, cloud_y_1 - 5), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_1 + 80, cloud_y_1), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_1 + 25, cloud_y_1 + 25), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_1 + 60, cloud_y_1 + 30), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_2, cloud_y_2), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_2 + 40, cloud_y_2 - 5), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_2 + 80, cloud_y_2), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_2 + 25, cloud_y_2 + 25), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_2 + 60, cloud_y_2 + 30), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_3, cloud_y_3), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_3 + 40, cloud_y_3 - 5), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_3 + 80, cloud_y_3), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_3 + 25, cloud_y_3 + 25), cloud1size)
    pygame.draw.circle(screen, cloud_colour, (cloud_x_3 + 60, cloud_y_3 + 30), cloud1size)
    # pygame.draw.rect(screen, (100, 100, 100), (building_x, building_y, 180, 270))
    # pygame.draw.rect(screen, window_sill, (building_x + 10, building_y + 13, 49, 69))
    # pygame.draw.rect(screen, window_colour, (building_x + 12, building_y + 15, 45, 65))
    # pygame.draw.rect(screen, window_sill, (building_x + 65, building_y + 13, 49, 69))
    # pygame.draw.rect(screen, window_colour, (building_x + 67, building_y + 15, 45, 65))
    # pygame.draw.rect(screen, window_sill, (building_x + 120, building_y + 13, 49, 69))
    # pygame.draw.rect(screen, window_colour, (building_x + 122, building_y + 15, 45, 65))
    # pygame.draw.rect(screen, window_sill, (building_x + 10, building_y + 91, 49, 69))
    # pygame.draw.rect(screen, window_colour, (building_x + 12, building_y + 93, 45, 65))
    # pygame.draw.rect(screen, window_sill, (building_x + 65, building_y + 91, 49, 69))
    # pygame.draw.rect(screen, window_colour, (building_x + 67, building_y + 93, 45, 65))
    # pygame.draw.rect(screen, window_sill, (building_x + 120, building_y + 91, 49, 69))
    # pygame.draw.rect(screen, window_colour, (building_x + 122, building_y + 93, 45, 65))
    pygame.draw.rect(screen, (122, 195, 175), (WIDTH - 130, HEIGHT - 258, 200, 250))
    pygame.draw.polygon(screen, (60, 60, 60), ((WIDTH - 330, HEIGHT - 258), (WIDTH, HEIGHT - 370), (WIDTH, HEIGHT - 258)))
    pygame.draw.rect(screen, dark_wood_colour, (WIDTH - 330, HEIGHT - 257, 20, 250))
    pygame.draw.rect(screen, dark_wood_colour, (WIDTH - 330, HEIGHT - 35, 200, 35))
    pygame.draw.rect(screen, light_wood_colour, (WIDTH - 310, HEIGHT - 150, 180, 25))
    pygame.draw.rect(screen, light_wood_colour, (WIDTH - 290, HEIGHT - 150, 20, 115))
    pygame.draw.rect(screen, light_wood_colour, (WIDTH - 250, HEIGHT - 150, 20, 115))
    pygame.draw.rect(screen, light_wood_colour, (WIDTH - 210, HEIGHT - 150, 20, 115))
    pygame.draw.rect(screen, light_wood_colour, (WIDTH - 170, HEIGHT - 150, 20, 115))
    pygame.draw.rect(screen, window_colour, (WIDTH - 105, HEIGHT - 220, 80, 110))
    pygame.draw.rect(screen, (75, 150, 15), (0, HEIGHT - 20, WIDTH, 80))

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
