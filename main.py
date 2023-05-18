import pygame
import sys
import random
import time

#Initialize Pygame
pygame.init()

#Set up the display
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Movement")

#Load the image sprite
sprite_image = pygame.transform.scale(pygame.image.load("images/sprite.png"),(100,100))
sprite_rect = sprite_image.get_rect()
sprite_speed = 5

#Set the initial position of the sprite
sprite_rect.x = screen_width // 2 - sprite_rect.width // 2
sprite_rect.y = screen_height // 2 - sprite_rect.height // 2

class Pokemon:
    def __init__(self, hp, name, moves, sprite):
      self.hp = hp
      self.name = name
      self.moves = moves
      self.sprite = sprite
    
    def attack(self, other, attack):
      if(random.randint(0,100)<=attack.accuracy):
        for i in range(10):
          self.sprite.x+=2
          time.wait(.05)
        for i in range(10):
          self.sprite.x-=2
          time.wait(.05)
        other.hp -= attack.damage+
         
        
      
          
          
#DISPLAYING TEXT
#font = pygame.font.Font('freesansbold.ttf', 32)
# create a text surface object,
# on which text is drawn on it.
#text = font.render('GeeksForGeeks', True, green, blue)
## create a rectangular object for the
# text surface object
# textRect = text.get_rect()
# # set the center of the rectangular object.
# textRect.center = (X // 2, Y // 2)
# copying the text surface object
# to the display surface object
# at the center coordinate.
#display_surface.blit(text, textRect)

class Attack:
    def init(self, accuracy, damage, name):
        self.name = name
        self.accuracy = accuracy
        self.damage = damage
    

#Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move the sprite
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        sprite_rect.x -= sprite_speed
    if keys[pygame.K_RIGHT]:
        sprite_rect.x += sprite_speed
    if keys[pygame.K_UP]:
        sprite_rect.y -= sprite_speed
    if keys[pygame.K_DOWN]:
        sprite_rect.y += sprite_speed

    # Draw the sprite and update the screen
    screen.fill((255, 255, 255))
    screen.blit(sprite_image, sprite_rect)
    pygame.display.flip()

#What graphics/UI stuff we need
# The battle stuff at bottom of the screen
  #when stuff clicked, changed the bottom of the screen to a new picture
#Pictures of both "pokemon"
#Other stuff
#