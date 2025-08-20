import pygame


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load("./assets/MenuBg.png")
        self.rect = self.surf.get_rect()

    def run(self):
        self.window.blit(source=self.surf, dest=self.rect)
        pygame.display.flip()
        pass