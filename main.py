import pygame, sys
from logger import log_state, log_event
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS festlegen
    clock = pygame.time.Clock() # clock-Objekt erzeugen 
    dt = 0 # Delta-Time festlegen

    updatable = pygame.sprite.Group() # Objekte die geupdated werden können
    drawable = pygame.sprite.Group() # Objekte die gezeichnet werden
    asteroids = pygame.sprite.Group() # Gruppe für Asteroiden
    shots = pygame.sprite.Group() # Gruppe für Bullets

    Player.containers = (updatable, drawable) # Player-Klasse den Gruppen hinzufügen
    Asteroid.containers = (asteroids, updatable, drawable) ## Asteroid-Klasse den Gruppen hinzufügen
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    # Player-Object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    AsteroidField()

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # prüfen ob Fenster geschlossen wurde
                return
            
        screen.fill("black") # fill screen black
        updatable.update(dt) # Updated alle Objekte in updatable-Gruppe
        for asteroid in asteroids:
            if player.collides_with(asteroid):
                log_event("player_hit")
                print("Game over!")
                sys.exit()

            for shot in shots:
                if asteroid.collides_with(shot):
                    log_event("asteroid_shot")
                    shot.kill()
                    asteroid.split()


        for sprite in drawable:
            # zeichnet alle Objekte in drawable-Gruppe
            sprite.draw(screen)

        pygame.display.flip() # refresh screen
        # Game-Loop Ende
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
