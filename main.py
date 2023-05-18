import sys
import os
import pygame
from pygame.locals import *
 
pygame.init()
 
fps = 60
fpsClock = pygame.time.Clock()
 
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

class Player(pygame.sprite.Sprite):
  def __init__(self):
    points = 0
   
# Game loop.
image_path = os.path.abspath(os.getcwd())+"images/"  # Replace with the path to your image file
image = pygame.image.load(image_path)
while True:
  screen.fill((0, 0, 0))
  player = Player()   # spawn player
  player.x = 0   # go to x
  player.y = 0   # go to y
  player_list = pygame.sprite.Group()
  player_list.add(player)
  for event in pygame.event.get():
    if event.type == QUIT:
      pygame.quit()
      sys.exit()
  
  # Update.
  
  # Draw.
  
  pygame.display.flip()
  fpsClock.tick(fps)