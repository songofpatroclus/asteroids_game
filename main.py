import pygame
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from logger import log_event
import sys

def main():
    pygame.init()

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    # Player is the name of the class, not an instance of it
    # This must be done before any Player objects are created   
    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    asteroids = pygame.sprite.Group()


    Asteroid.containers = (asteroids,updatable, drawable)
    AsteroidField.containers = (updatable,)
    asteroid_field = AsteroidField()

    while True:
        

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        # You may also call the .update() method for every member of a group by calling it on the group itself:
        updatable.update(dt)

        for obj in asteroids:
            if player.collides_with(obj):
                log_event("player_hit")
                print("Game Over!")
                sys.exit()

        screen.fill("black")
        # You can iterate over objects in a group just like any other collection in Python:
        for obj in drawable:
            obj.draw(screen)



        pygame.display.flip()

        

        # limit the framerate to 60 FPS
        dt = clock.tick(60) / 1000
        log_state()


if __name__ == "__main__":
    main()
