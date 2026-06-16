import pygame

from .window_abc import WindowABC 


class Window(WindowABC):
    def __init__(self, title, width, height):
        self.title = title
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.running = True
        self.clock = pygame.time.Clock()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            else:
                yield event 

    def fill(self, color):
        self.screen.fill(color)

    def draw(self, surface, rect):
        self.screen.blit(surface, rect)

    def display(self):
        pygame.display.flip()
        self.clock.tick(60)

    def stop(self): self.running = False
    
    def start(self): self.running = True


    def size(self):
        return self.width, self.height