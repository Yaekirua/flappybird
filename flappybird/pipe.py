import pygame
import random

PIPE_GAP = 100

class Pipe:
    def __init__(self, image_path, x):
        self.image = pygame.image.load(image_path)
        self.rect_top = self.image.get_rect(midbottom=(x, random.randint(100, 400)))
        self.rect_bottom = self.image.get_rect(midtop=(x, self.rect_top.bottom + PIPE_GAP))
        
    def update(self): 
        self.rect_top.x -= 5
        self.rect_bottom.x -= 5
        
    def draw(self, screen):
        screen.blit(self.image, self.rect_top)
        screen.blit(self.image, self.rect_bottom)
        
        
    def is_off_screen(self):
        return self.rect_top.right < 0
    
    def collides_with(self, bird):
        return self.rect_top.colliderect(bird.rect) or self.rect_bottom.colliderect(bird.rect)
    
    