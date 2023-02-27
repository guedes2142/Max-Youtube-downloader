from pygame.locals import *
import pygame
pygame.init()
   
def playsound():
    
 
    pygame.mixer.music.load('123.mp3')
    pygame.mixer.music.play(-1)
    pygame.mixer.music.set_volume(0.2)
    
def stopSong():
    
   pygame.mixer.music.stop()
   


