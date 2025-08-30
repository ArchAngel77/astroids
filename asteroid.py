
import random
import pygame
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        CircleShape.__init__(self, x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, (255,255,255), (int(self.position.x), int(self.position.y)), int(self.radius), 2)

    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        child_radius = self.radius - ASTEROID_MIN_RADIUS
        angle = random.uniform(20,50)
        v1 = self.velocity.rotate(angle) * 1.2
        v2 = self.velocity.rotate(-angle) * 1.2

        a1 = Asteroid(self.position.x, self.position.y, child_radius)
        a1.velocity = v1

        a2 = Asteroid(self.position.x, self.position.y, child_radius)
        a2.velocity = v2
