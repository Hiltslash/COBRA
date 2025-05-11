import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame

def startup(color, name, sx, sy, closable=True):
    pygame.init()
    screen = pygame.display.set_mode((sx, sy))
    clock = pygame.time.Clock()
    running = True
    dt = 0
    screen.fill(color)
    pygame.display.set_caption(name)
    while running:
        # poll for events
        # pygame.QUIT event means the user clicked X to close your window
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                if closable:
                    running = False
                else:
                    running = True

        # fill the screen with a color to wipe away anything from last frame
        screen.fill("purple")

        # RENDER YOUR GAME HERE

        # flip() the display to put your work on screen
        pygame.display.flip()

        clock.tick(60)  # limits FPS to 60

    pygame.quit()

if __name__ == "__main__":
    startup((255, 154, 84), "HEHE", 1000, 600, True)