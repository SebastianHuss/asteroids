import pygame
from logger import log_state
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player

def main():
    print(f"Starting Asteroids with pygame version: {pygame.version.ver}")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # FPS festlegen
    clock = pygame.time.Clock() # clock-Objekt erzeugen 
    dt = 0 # Delta-Time festlegen

    # Player-Object
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # prüfen ob Fenster geschlossen wurde
                return
            
        screen.fill("black") # fill screen black
        player.draw(screen)
        player.update(dt)

        pygame.display.flip() # refresh screen
        # Game-Loop Ende
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()
