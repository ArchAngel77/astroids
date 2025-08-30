
import pygame
from constants import PLAYER_SPEED
from circleshape import CircleShape
from shot import Shot
from constants import PLAYER_SHOOT_SPEED
import constants

class Player(CircleShape):
    def __init__(self, x, y):
        super().__init__(x, y, constants.PLAYER_RADIUS)
        self.rotation = 0
        self.cooldown = 0

    def move(self, dt):
        forward = pygame.Vector2(0,1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt

    def rotate(self, dt):
        self.rotation = self.rotation + (constants.PLAYER_TURN_SPEED * dt)


    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right
        return [a, b, c]

    def shoot(self):
        if self.cooldown > 0:
            return
        direction = pygame.Vector2(0,1).rotate(self.rotation)
        velocity = direction * constants.PLAYER_SHOOT_SPEED
        Shot(self.position, velocity)
        self.cooldown = constants.PLAYER_SHOOT_COOLDOWN

    def draw(self, screen):
        white = (255, 255, 255)
        pygame.draw.polygon(screen, white, self.triangle(), 2)

    def update(self, dt):
        self.cooldown = max(0, self.cooldown - dt)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.rotate(-dt)
        if keys[pygame.K_d]:
            self.rotate(dt)
        if keys[pygame.K_w]:
            self.move(dt)
        if keys[pygame.K_s]:
            self.move(-dt)
        if keys[pygame.K_SPACE]:
            self.shoot()

