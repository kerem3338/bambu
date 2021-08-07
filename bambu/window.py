import pygame
import pymsgbox
class Window:
    def __init__(self):
        pygame.init()
        

    def alert(self, message, title):
        pymsgbox.alert(message, title)
