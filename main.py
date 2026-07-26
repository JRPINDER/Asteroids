import pygame
from constants import *
from logger import log_state, log_event
from player import *
from asteroid import *
from asteroidfield import *
from circleshape import *
import sys

def main():
    pygame.init()
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0.0

    asteroids = pygame.sprite.Group()
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    AsteroidField.containers = (updatable,)
    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    Shot.containers = (shots, drawable, updatable)

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    AsteroidField()

    while True:
        screen.fill("black")
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            pass
        for drawing in drawable:
            drawing.draw(screen)
        for updates in updatable:
            updates.update(dt)
        for asty in asteroids:
            if player.collides_with(asty):
                log_event("player_hit")
                print("Game over!")
                sys.exit()
        for asty in asteroids:
            for shot in shots:
                if shot.collides_with(asty):
                    log_event("asteroid_shot")
                    shot.kill()
                    asty.split()
        pygame.display.flip()
        dt = clock.tick(60)/1000

if __name__ == "__main__":
    main()
