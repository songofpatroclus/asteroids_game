from logger import log_event
import circleshape
import pygame
import constants
import random

class Asteroid(circleshape.CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, constants.LINE_WIDTH)
    
    def update(self, dt):
        self.position += self.velocity * dt

    def split(self):
        self.kill()
        if self.radius <= constants.ASTEROID_MIN_RADIUS:
            return
        else:
            log_event("asteroid_split")
            new_angle = random.uniform(20,50)
            asteroid1 = Asteroid(self.position.x, self.position.y, constants.ASTEROID_MIN_RADIUS)
            asteroid1.velocity = self.velocity.rotate(new_angle) * 1.2
            asteroid2 = Asteroid(self.position.x, self.position.y, self.radius - constants.ASTEROID_MIN_RADIUS)
            asteroid2.velocity = self.velocity.rotate(-new_angle)






