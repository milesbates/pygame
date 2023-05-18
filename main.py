import pygame
import sys

#Initialize Pygame
pygame.init()

#Set up the display
screen_width, screen_height = 1000, 1000
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Sprite Movement")

#Load the image sprite
sprite_image = pygame.image.load("sprite.png")
sprite_rect = sprite_image.get_rect()
sprite_speed = 5

#Set the initial position of the sprite
sprite_rect.x = screen_width // 2 - sprite_rect.width // 2
sprite_rect.y = screen_height // 2 - sprite_rect.height // 2

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