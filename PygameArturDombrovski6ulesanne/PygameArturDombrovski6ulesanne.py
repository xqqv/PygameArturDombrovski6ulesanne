
import pygame
pygame.init()

# Colors
red = [255, 0, 0]
LBlue = [153, 204, 255]

# Screen settings
screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Klaviatuuriga juhtimine")  # "Keyboard control"
screen.fill(LBlue)
clock = pygame.time.Clock()

# Coordinates and speed
posX, posY = screenX / 2, screenY / 2
speedX, speedy = 0, 0

gameover = False

while not gameover:
    clock.tick(60)  
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
            gameover = True
        elif event.type == pygame.KEYDOWN:  
            if event.key == pygame.K_RIGHT:  
                speedX = 3
            elif event.key == pygame.K_LEFT:  
                speedX = -3
            elif event.key == pygame.K_UP:  
                speedy = -3
            elif event.key == pygame.K_DOWN:  
                speedy = 3

    
    posX += speedX
    posY += speedy

    screen.fill(LBlue)
  
    pygame.draw.rect(screen, red, [posX, posY, 30, 30])
   
    pygame.display.flip()

pygame.quit()

#6

import pygame
import sys


pygame.init()

screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("PingPong")
clock = pygame.time.Clock()


white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)


paddle_width = 100
paddle_height = 10
paddle_speed = 10
paddle = pygame.Rect(screenX // 2 - paddle_width // 2, screenY - 20, paddle_width, paddle_height)

ball_size = 20
ball = pygame.Rect(screenX // 2 - ball_size // 2, screenY // 2 - ball_size // 2, ball_size, ball_size)
ball_speed_x = 3
ball_speed_y = 3

gameover = False

while not gameover:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

  
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and paddle.left > 0:
        paddle.x -= paddle_speed
    if keys[pygame.K_RIGHT] and paddle.right < screenX:
        paddle.x += paddle_speed


    ball.x += ball_speed_x
    ball.y += ball_speed_y
    
    if ball.left <= 0 or ball.right >= screenX:
        ball_speed_x = -ball_speed_x
    if ball.top <= 0:
        ball_speed_y = -ball_speed_y

   
    if ball.colliderect(paddle):
        ball_speed_y = -ball_speed_y

    if ball.bottom >= screenY:
        gameover = True

   
    screen.fill(black)
    pygame.draw.rect(screen, blue, paddle)
    pygame.draw.ellipse(screen, red, ball)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

#7
import pygame
import random

pygame.init()

red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
light_green = [153, 255, 153]
light_blue = [153, 204, 255]

screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Hiir")
screen.fill(light_blue)

clock = pygame.time.Clock()
gameover = False

while not gameover:
    clock.tick(10)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    
  
    if pygame.mouse.get_pressed()[0]: 
        click = pygame.mouse.get_pos()
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        varv = [r, g, b]
        ruuduke = pygame.Rect(click[0] - 50, click[1] - 50, 100, 100) 
        pygame.draw.rect(screen, varv, ruuduke)
    
    pygame.display.flip()
    screen.fill(light_blue)

pygame.quit()

#8

import pygame
import random

pygame.init()

# Värvid
red = [255, 0, 0]
green = [0, 255, 0]
blue = [0, 0, 255]
pink = [255, 153, 255]
light_green = [153, 255, 153]
light_blue = [153, 204, 255]

screenX = 640
screenY = 480
screen = pygame.display.set_mode([screenX, screenY])
pygame.display.set_caption("Ringide Mäng")
screen.fill(light_blue)

clock = pygame.time.Clock()
gameover = False

ringe = []
max_ringe = 10
algus_raadius = 10

while not gameover:
    clock.tick(30)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameover = True
    
    if pygame.mouse.get_pressed()[0]:  
        click = pygame.mouse.get_pos()
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        varv = [r, g, b]
        
        if len(ringe) >= max_ringe:
            ringe.pop(0)  
        ringe.append({"pos": click, "varv": varv, "raadius": algus_raadius})

    screen.fill(light_blue)  
    
    
    for ring in ringe:
        pygame.draw.circle(screen, ring["varv"], ring["pos"], ring["raadius"])
        ring["raadius"] += 1  

    pygame.display.flip()

pygame.quit()
