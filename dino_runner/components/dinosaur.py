import pygame
from pygame.sprite import Sprite
from pygame import Surface
from dino_runner.utils.constants import RUNNING, JUMPING, DUCKING


DINO_JUMPING = "JUMPING"
DINO_RUNNING = "RUNNING"
DINO_DUCKING = "DUCKING"


class Dinosaur(Sprite):
    POS_X = 80
    POS_Y = 310
    JUMP_VELOCITY = 8.5
    
    def __init__(self):
        self.image = RUNNING[0]
        self.position()
        self.step = 0
        self.action = DINO_RUNNING
        self.jump_velocity = self.JUMP_VELOCITY 

    def update(self, user_input):
        if self.action == DINO_RUNNING:
            self.run()
        elif self.action == DINO_JUMPING:
            self.jump()
        elif self.action == DINO_DUCKING:
            self.duck()
            
        if self.action != DINO_JUMPING:
            if user_input[pygame.K_UP]:
                self.action = DINO_JUMPING
        if self.action != DINO_JUMPING and DINO_RUNNING:
            if user_input[pygame.K_DOWN]:
                self.action = DINO_DUCKING
            else: 
                self.action = DINO_RUNNING

        if self.action == DINO_DUCKING:
            self.rect.y = self.POS_Y + 40
        
        if self.step >= 10:
            self.step = 0
            
    def run(self):
        self.image = RUNNING[self.step // 5]
        self.position()
        self.step += 1  

    def jump(self):
        self.image = JUMPING
        self.rect.y -= self.jump_velocity * 4 
        self.jump_velocity -= 0.8 

        if self.jump_velocity < -self.JUMP_VELOCITY:
            self.action = DINO_RUNNING
            self.rect.y = self.POS_Y
            self.position()

    def duck(self):
        self.image = DUCKING[self.step // 5]
        self.position()
        self.step += 1

    def position(self):
        self.rect = self.image.get_rect()
        self.rect.x = self.POS_X
        self.rect.y = self.POS_Y
        self.jump_velocity = self.JUMP_VELOCITY


    def draw(self, screen: Surface):
        screen.blit(self.image, (self.rect.x, self.rect.y))

