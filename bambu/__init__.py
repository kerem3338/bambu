#Bambu Engine By Zoda
import os
import sys

#Pygame welcome message hide
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "1"

import pygame
import time
import keyboard
import bambu.engine_config
import bambu.colors
import bambu.window
import bambu.ui
import bambu.network
from pathlib import Path




if sys.version_info < (3, 8):
    print("Bambu, python un 3.8 veya daha yüksek bir sürümün kullanımı için hazırlandı devam etmeniz halinde bazı sorunlar ile karşılaşabilirsiniz")

class bambu:
    def __init__(self):
        #Engine Configuretion
        pygame.init()
        self.network = network.Network()
        self.ui = ui.Ui()
        self.window = window.Window()
        self.welcome_text = engine_config.welcome
        self.version = engine_config.engine_version

        #icon
        self.SOURCEPATH = Path(__file__).parents[0]

        #self.icon = engine_config.engine_icon
        self.icon = os.path.abspath(os.path.join(self.SOURCEPATH, "icon.png"))
        
        
        self.baslik = engine_config.normal_title
        self.boyutlar = None, None
        self.ekran = None
        self.engine_running = False
        
        self.engine_path = os.getcwd()

        self.ses_durum = None
        self.pause = False
        

        #Welcome text
        print(self.welcome_text)
        
    #Engine version
    def ver(self):
        return self.version

    
    #Start engine window 
    def engine_init(self, width=500, height=500): #width=genişlik height=yükseklik
        self.engine_running = self.engine_running = True
        
        pygame.display.set_caption(self.baslik)
        icon = pygame.image.load(self.icon.replace("\\", "\\\\"))
        
        pygame.display.set_icon(icon)
        self.boyutlar = width, height
        
        a = (self.boyutlar[0], self.boyutlar[1])
        try:
            self.ekran = pygame.display.set_mode(a)
        except TypeError:
            print("(engine_init) TypeEror: String  kabul edilmiyor (Sadece İntiger Kabul ediliyor)")



    def get_screen_size(self):
        if self.boyutlar[0] == None and self.boyutlar[1] == None:
            print("Engine not inited")
        else:
            return self.boyutlar[0], self.boyutlar[1]
    
    def hide_console(self):
        self.window.hide_console()

    
    
    #motor için dosya Yolu yapılandırması
    def set_engine_path(self, path):
        os.chdir(path)
        self.engine_path = self.engine_path = path

    #return engine path
    def get_engine_path(self):
        return self.engine_path

    
    #---sound---#
    def music_play(self, sound, repeat=False, play_time=None):
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
        if self.ses_durum == True:
            pygame.mixer.music.stop() 
            self.ses_durum = self.ses_durum = False
        else:
            print("(music_stop): Ses dosyası zaten durdurulmuş")

    
    
        
    def music_pause(self):
        self.pause = self.pause = True
        pygame.mixer.music.pause()
        
    def music_unpause(self):
        self.pause = self.pause = False
        pygame.mixer.music.unpause()
    #---sound---#
    
    #--Network--#
    def internet_required(self, error=None):
        if error is None:
            self.network.internet_required()
        else:
            self.network.internet_required(error)
    #--Network--#
    
    #---ui---#
    def load_image(self, image, x, y):
        self.ui.load_image(self.ekran, image, x, y)
        
    def screen_update(self):
        pygame.display.update()

    def clear_screen(self):
        self.ui.clear_screen(self.ekran)
        
    def draw_circle(self, color, x, y, size):
        self.ui.draw_circle(self.ekran, color, x, y, size)
    #---ui---#


        
    #Set background color with color list
    def background_color(self, color):
        color_list = colors.color_list
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
        

    def alert(self, message, title="Bambu Engine"):
        self.window.alert(message, title)

    def set_title(self, baslik=str):
        self.baslik = baslik
        pygame.display.set_caption(self.baslik)

    
    def take_screenshoot(self, filename):
        screen = pygame.Surface((self.boyutlar[0], self.boyutlar[1]))
        pygame.image.save(screen, filename)

    def set_window_size(self, width=int, height=int):
        self.boyutlar = self.boyutlar = width, height
        a = (self.boyutlar[0], self.boyutlar[1])
        self.ekran = self.ekran = pygame.display.set_mode(a)
        pygame.display.update()
    
    def load_icon(self, icon):
        self.icon = icon
        pygame.display.update()

    def engine_stop(self):
        if self.engine_running == True:
            self.engine_running = False
            pygame.quit()
        elif not self.engine_running:
            print("(engine_stop): Motor Zaten Kapalı Durumda")


    #pygame.event
    def loop(self):
        while True:
            try:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
            except pygame.error:
                pass
            except:
                exit()
    

    

#5/7/2021 - başlangıç
#14/8/2021 - geliştirme
#0/0/0000 - bitiş
