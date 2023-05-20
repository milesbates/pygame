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
#sprite_image = pygame.transform.scale(pygame.image.load("images/EagleSprite.jpg"),(100,100))
#sprite_rect = sprite_image.get_rect()
#sprite_speed = 5

#Set the initial position of the sprite
#sprite_rect.x = screen_width // 2 - sprite_rect.width // 2
#sprite_rect.y = screen_height // 2 - sprite_rect.height // 2

class Pokemon:
    def __init__(self, hp, name, moves, sprite, potions):
      self.hp = hp
      self.name = name
      self.moves = moves
      self.sprite = sprite
      self.potions = potions #amount of potions
      self.rect = self.sprite.get_rect()
    def attack(self, other, attack):
      if(random.randint(0,100)<=attack.accuracy):
        for i in range(10):
          self.sprite.x+=2
          time.wait(.05)
        for i in range(10):
          self.sprite.x-=2
          time.wait(.05)
        other.hp -= attack.damage
      else:
        display_text(attack.name + 'missed the opponent!')
    def itemuse(self):
      self.potions-=1
       

def display_text(text, screen):
   red = (255, 0, 0)
   
   font = pygame.font.Font('freesansbold.ttf', 32)
   text = font.render(text, True, red) 
   textRect = text.get_rect()      
   textRect.center = (500, 200)   
   screen.blit(text, textRect)
          
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
#

class Attack:
    def __init__(self, accuracy, damage, name):
        self.name = name
        self.accuracy = accuracy
        self.damage = damage
    




EagleMoves = [Attack(accuracy = 95, damage = 20, name = "Scratch"), Attack(accuracy = 70, damage = 40, name = "Feather Frenzy"), Attack(accuracy = 85, damage = 30, name = "Sonic Screech"), Attack(accuracy = 90, damage = 25, name = "Wind Talons")]
Eagle = Pokemon(hp = 100, name = "ESD Eagle", moves = EagleMoves, sprite = pygame.transform.scale(pygame.image.load("images/Sprites/EagleSprite.jpg"),(250,250)),potions = 2)

LionMoves = [Attack(accuracy = 80, damage = 35, name ='Royal Roar'), Attack(accuracy = 65, damage = 45, name ='Savanna Slam'), Attack(accuracy = 100, damage = 15, name ='Kings Claw'), Attack(accuracy = 50, damage = 50, name ='Pride Pounce')]
Lion = Pokemon(hp = 100, name = "St. Marks Lion", moves = LionMoves, sprite = pygame.transform.scale(pygame.image.load("images/Sprites/LionSprite.jpg"),(100,100)), potions = 0)
ui = Pokemon(hp = 0, name = 'ui', moves = [], sprite = pygame.transform.scale(pygame.image.load("images/GUI/MainUI.png"),(1000,300)), potions = 0)



DisplayList = []
def gameStart(pMon1 = Eagle, pMon2 = Lion):
   pMon1.rect.x = 200
   pMon1.rect.y = 400
   pMon2.rect.x = 800
   pMon2.rect.y = 200
   
   ui.rect.x = 0
   ui.rect.y = 700
   DisplayList = [[Eagle.sprite, Eagle.rect], [Lion.sprite,Lion.rect], [ui,ui.rect]]
   
gameStart()



#display_text('TEST')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
          mouse_presses = pygame.mouse.get_pressed()
          if mouse_presses[0]:
            pos = pygame.mouse.get_pos()
            print(pos)
            if(pos[1] <= 850 and pos[1] >= 700 ):
               print('fight')#update ui
            if(pos[1]<=1000 and pos[1] >= 850 and pos[0] >=0 and pos[0] <= 500):
               print('bag')
            if(pos[1]<=1000 and pos[1] >= 850 and pos[0] >=500 and pos[0] <= 1000):
               print('run')
               

    # Move the sprite
    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     sprite_rect.x -= sprite_speed
    # if keys[pygame.K_RIGHT]:
    #     sprite_rect.x += sprite_speed
    # if keys[pygame.K_UP]:
    #     sprite_rect.y -= sprite_speed
    # if keys[pygame.K_DOWN]:
    #     sprite_rect.y += sprite_speed

    # Draw the sprite and update the screen
    screen.fill((255, 255, 255))
    # for im in DisplayList:
    #   screen.blit(im[0], im[1])
    
    screen.blit(Eagle.sprite, Eagle.rect)
    screen.blit(Lion.sprite, Lion.rect)
    screen.blit(ui.sprite, ui.rect)
    display_text('TEST', screen)
    pygame.display.flip()

#What graphics/UI stuff we need
# The battle stuff at bottom of the screen
  #when stuff clicked, changed the bottom of the screen to a new picture
#Pictures of both "pokemon"
#Other stuff
#