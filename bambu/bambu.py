#Bambu Engine by Zoda
import os

#Pygame welcome message hide
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

import pygame
import sys
import time
import keyboard
import engine_config

if sys.version_info < (3, 8):
    print("Lütfen Python Sürümünüzü 3.8 yada yüksek bir sürüme yükseltin yoksa bazı hatalar ile karşılaşabilirsiniz")
class bambu:
    
    def __init__(self):
        #Engine Configuretion
        pygame.init()
        self.welcome_text = engine_config.welcome
        self.icon = engine_config.engine_icon
        self.version = engine_config.engine_version

        
        self.baslik = "Bambu Engine"
        self.boyutlar = None, None
        self.ekran = None
        self.engine_running = False
        


        self.ses = None
        self.pause = False
        self.ses_düzeyi = 1.0

        #Note: welcome message will be added in next version
        print(self.welcome_text)
        
    #Engine version
    def ver(self):
        print(self.version)

    # 
    def engine_init(self, width=int, height=int): #width=genişlik height=yükseklik
        self.engine_running = self.engine_running = True
        
        pygame.display.set_caption(self.baslik)
        icon = pygame.image.load(self.icon)
        
        pygame.display.set_icon(icon)
        self.boyutlar = width, height
        
        a = (self.boyutlar[0], self.boyutlar[1])
        try:
            self.ekran = pygame.display.set_mode(a)
        except TypeError:
            print("(engine_init) TypeEror: String  kabul edilmiyor (Sadece İntiger Kabul ediliyor)")
        
            
    
        
    #---ses/müzik---#
    def music_play(self, sound, repeat=False):
        pygame.mixer.init()
        if not repeat:
            self.ses_durum = self.ses_durum = True
            try:
                pygame.mixer.music.load(sound) 
                pygame.mixer.music.play()
            except pygame.error:
                print("(play) Pygame.error: Ses Dosyası bulunduğunuz dosya konumunda bulunamadı")
            self.ses_durum = self.ses_durum  = False
        else:
            self.ses_durum = self.ses_durum = True
            try:
                pygame.mixer.music.load(sound) 
                pygame.mixer.music.play(-1)
            except pygame.error:
                print("(play) Pygame.error: Ses Dosyası bulunduğunuz dosya konumunda bulunamadı")
                
    def music_stop(self):
        if self.ses_durum.isdigit() == "True":
            pygame.mixer.music.stop() 
            self.ses_durum = self.ses_durum = False
            
    def music_pause(self):
        self.pause = self.pause = True
        pygame.mixer.music.pause()
        
    def music_unpause(self):
        self.pause = self.pause = False
        pygame.mixer.music.unpause()
    #---ses/müzik---#

    def screen_update(self):
        pygame.display.update()


    #Set background color with color list
    def background_color(self, color):
        color_list = {
            "red": (255, 0, 0),
            "blue": (0, 0, 255),
            "green": (0, 255, 0),
            "orange": (255, 165, 0),
            "light silver": (192, 192, 192),
            "light gray": (211,211,211),
            "black": (0, 0, 0),
            "gold": (255,215,0),
            "yellow": (255,255,0),
            
        }
        if color in color_list:
            try:
                self.ekran.fill(color_list[color])
                pygame.display.update()
            except ValueError:
                print("(background_color) ValueError: Geçersiz renk ergümanı")
            except AttributeError:
                print("(background_color) AttributeError: Engine_init başlatma hatası")
        else:
            print("(background_color): Renk tanımlı Değil")

    #set background color with rgb
    def background_color_rgb(self, rgb1, rgb2, rgb3):
        color = (rgb1, rgb2, rgb3)
        try:
            self.ekran.fill(color)
            pygame.display.update()
        except ValueError:
            print("(background_color) ValueError: Geçersiz renk ergümanı")
        except AttributeError:
            print("(background_color) AttributeError: Engine_init başlatma hatası")

    def set_title(self, baslik=str):
        self.baslik = baslik
        pygame.display.set_caption(self.baslik)
        
    def set_window_size(self, width=int, height=int):
        self.boyutlar = self.boyutlar = width, height
        a = (self.boyutlar[0], self.boyutlar[1])
        
    def load_icon(self, icon):
        self.icon = icon
        pygame.display.update()

    def engine_stop(self):
        if self.engine_running == True:
            self.engine_running = False
            pygame.quit()
        elif not self.engine_running:
            print("(engine_stop): Zaten Motor Kapatılmış")
   

#5/7/2021 - başlangıç
#21/7/2021 - geliştirme
#0/0/0000 - bitiş
