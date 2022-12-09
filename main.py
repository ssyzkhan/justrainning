import pygame,sys
from settings import *
class Main:
    def __init__(self):
        pygame.init()
        self.window_surface = pygame.display.set_mode((WINDOW_WIDTH,WINDOW_HEIGHT))
    def run(self):
        while True:
            pass
if __name__=='__main__':
    main = Main()
    main.run()

 
