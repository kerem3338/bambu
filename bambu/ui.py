import pygame
import bambu.colors

class Ui:
    def __init__(self):
        pygame.init()
        self.col = bambu.colors.color_list
        
    
    def load_image(self, screen, image, x, y):
        image = pygame.image.load(image)
        screen.blit(image,(x, y))
        pygame.display.update()

            
    def draw_circle(self, screen, color, x, y, size):
        if color in self.col:
            pygame.draw.circle(screen, (color),(x, y), size)
            pygame.display.update()
        else:
            print(f"draw_circle: {color} bulunamadı")
            
    def clear_screen(self, screen):
        screen.fill((0, 0, 0))
        pygame.display.update()
