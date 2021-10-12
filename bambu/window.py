import pygame
import pymsgbox
try:
    import win32gui, win32con
except:
    print("Lütfen pywin32 paketini kurun (kurulu olmadan da motor çalışır ama hide_console() ögesini kullanmazsınız!")

class Window:
    def __init__(self):
        pygame.init()
        

    def alert(self, message, title):
        pymsgbox.alert(message, title)

    
    def hide_console(self):
        #Uyarı hide console sadece kodu çalıştıran uygulamayı gizler
        #yani vs code veya farklı bir ide den kodu çalıştırsanız ide penceresini gizler ama ide hala çalışır vaziyettedir
        hide = win32gui.GetForegroundWindow()
        win32gui.ShowWindow(hide , win32con.SW_HIDE)

    
