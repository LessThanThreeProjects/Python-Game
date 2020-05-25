import pygame
import numpy as np
from pygame.sprite import Sprite

class Alien(Sprite):
    #Represents a single alien
    def __init__(self, ai_game):
        super().__init__()
        self.ai_game = ai_game
        self.settings = self.ai_game.settings
        self.screen = ai_game.screen
        self.alien1 = pygame.image.load('images/alien1.png')
        self.alien2 = pygame.image.load('images/alien2.png')
        self.rect1 = self.alien1.get_rect()
        self.rect2 = self.alien2.get_rect()
        self.rect1.x = self.ai_game.ship.rect.x + np.random.randint(100, 300)
        self.rect1.y = self.ai_game.ship.rect.y + np.random.randint(100, 300)
        self.rect2.x = self.ai_game.ship.rect.x + np.random.randint(300, 500)
        self.rect2.y = self.ai_game.ship.rect.y + np.random.randint(300, 500)
        self.type = ''
        self.rect = ''

    def draw_alien(self):
        #Draw each alien
        if self.type == 1:
            self.screen.blit(self.alien1, self.rect1)
        elif self.type == 2:
            self.screen.blit(self.alien2, self.rect2)

    def update(self):
        if self.type == 1:
            if self.rect1.x < self.ai_game.ship.rect.x:
                self.rect1.x += self.settings.alien1_speed
            elif self.rect1.x > self.ai_game.ship.rect.x:
                self.rect1.x -= self.settings.alien1_speed
            if self.rect1.y < self.ai_game.ship.rect.y:
                self.rect1.y += self.settings.alien1_speed
            elif self.rect1.y > self.ai_game.ship.rect.y:
                self.rect1.y -= self.settings.alien1_speed
        elif self.type == 2:
            if self.rect2.x < self.ai_game.ship.rect.x:
                self.rect2.x += self.settings.alien1_speed
            elif self.rect2.x > self.ai_game.ship.rect.x:
                self.rect2.x -= self.settings.alien1_speed
            if self.rect2.y < self.ai_game.ship.rect.y:
                self.rect2.y += self.settings.alien1_speed
            elif self.rect2.y > self.ai_game.ship.rect.y:
                self.rect2.y -= self.settings.alien1_speed