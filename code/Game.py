import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.Menu import Menu


class Game:
    def __init__(self):
        pygame.init()
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()


            # CHECK FOR ALL EVENTS
            # for event in pygame.event.get():
            #    if event.type == pygame.QUIT:
            #         pygame.quit()  # CLOSE THE WINDOW
            #         quit()
