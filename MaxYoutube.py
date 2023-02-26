
# Rafael guedes
# github.com/guedes2142

from pytube import YouTube
from time import sleep
import time
from rich.progress import track
import os
from pytube import Search
from colorama import Fore, Style
import pygame
from pygame.locals import *
# colors
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"
# path
# SAVE_PATH = 'C:/Users/Rafael/Desktop'
# banner
text = 'thanks for use me'
print(CYAN + f'[{text:*^88}]' + RESET)
print(RED + '███╗░░░███╗░█████╗░██╗░░██╗   ██╗░░░██╗░█████╗░██╗░░░██╗████████╗██╗░░░██╗██████╗░███████╗' + RESET)
print(RED + '████╗░████║██╔══██╗╚██╗██╔╝  ╚██╗░██╔╝██╔══██╗██║░░░██║╚══██╔══╝██║░░░██║██╔══██╗██╔════╝' + RESET)
print(RED + '██╔████╔██║███████║░╚███╔╝░  ░╚████╔╝░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██████╦╝█████╗░░' + RESET)
print(RED + '██║╚██╔╝██║██╔══██║░██╔██╗░  ░░╚██╔╝░░██║░░██║██║░░░██║░░░██║░░░██║░░░██║██╔══██╗██╔══╝░░' + RESET)
print(RED + '██║░╚═╝░██║██║░░██║██╔╝╚██╗  ░░░██║░░░╚█████╔╝╚██████╔╝░░░██║░░░╚██████╔╝██████╦╝███████╗' + RESET)
print(RED + '╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ░░░╚═╝░░░░╚════╝░░╚═════╝░░░░╚═╝░░░░╚═════╝░╚═════╝░╚══════╝' + RESET)

print(GREEN + '██████╗░░█████╗░███╗░░██╗░██╗░░░░░░░██╗██╗░░░░░░█████╗░░█████╗░██████╗░███████╗██████╗░' + RESET)
print(GREEN + '██╔══██╗██╔══██╗████╗░██║░██║░░██╗░░██║██║░░░░░██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗' + RESET)
print(GREEN + '██║░░██║██║░░██║██╔██╗██║░╚██╗████╗██╔╝██║░░░░░██║░░██║███████║██║░░██║█████╗░░██████╔╝' + RESET)
print(GREEN + '██║░░██║██║░░██║██║╚████║░░████╔═████║░██║░░░░░██║░░██║██╔══██║██║░░██║██╔══╝░░██╔══██╗' + RESET)
print(GREEN + '██████╔╝╚█████╔╝██║░╚███║░░╚██╔╝░╚██╔╝░███████╗╚█████╔╝██║░░██║██████╔╝███████╗██║░░██║' + RESET)
print(GREEN + '╚═════╝░░╚════╝░╚═╝░░╚══╝░░░╚═╝░░░╚═╝░░╚══════╝░╚════╝░╚═╝░░╚═╝╚═════╝░╚══════╝╚═╝░░╚═╝' + RESET)
print(BLUE + 'by.Rafael Guedes' + RESET)
print(CYAN + 'github.com/guedes2142' + RESET)
print()
print(RED + 'Obs: maybe you video dont have some resolutions and this may cause problems' + RESET)
print(Fore.YELLOW + 'Downloading copyrighted YouTube videos is illegal!\n '
    'I am not responsible for your downloads! Go at your own risk!' + Style.RESET_ALL)


pygame.init()
musicafundo = pygame.mixer.music.load('123.mp3')
pygame.mixer.music.play(-1)


while True:
    
    
    print(GREEN + 'note:The file will be saved in the same folder as this app ' + RESET)
    print()
    # options
    print(RED + 'choose an option' + RESET)
    print(GREEN + '1: Video download' + RESET)
    print(BLUE + '2: Video only audio.mp4' + RESET)
    print(GREEN + '3: Search' + RESET)
    print(RED + '4: exit' + RESET)
    print()
    choice = input('')
    print()
    '''
    if choice =='3': #TODO: ver como pega o resultado e usar as opções para download
        searchChoice = input('')
        s = Search('YouTube Rewind')
        print(s.results)
        continue
    '''

    if choice == '1':
        print('Choose a resolution [1080],[720],[360] ')
        resolution = input()
        
        if resolution == '1080':
            try:
                print(GREEN + 'Insert the video link' + RESET)
                videoLink = str(input())
                yt = YouTube(f'{videoLink}')
                for i in track(range(10), description="Downloading..."):
                    time.sleep(1)  # Simulate work being done
                stream = yt.streams.get_by_itag(137)
                stream.download()
            except:
                print('Conexion error,or please try 720 or 360 px')
                break
            print(GREEN + 'Success' + RESET)
            continue

        elif resolution == '720':
            try:
                print(GREEN + 'Insert the video link' + RESET)
                videoLink = str(input())
                yt = YouTube(f'{videoLink}')
                for i in track(range(10), description="Downloading..."):
                    time.sleep(1)  # Simulate work being done
                stream = yt.streams.get_by_itag(22)
                stream.download()
            except:
                print('Conexion error')
                break
            print(GREEN + 'Success' + RESET)
            continue

        elif resolution == '360':
            try:
                print(GREEN + 'Insert the video link' + RESET)
                videoLink = str(input())
                yt = YouTube(f'{videoLink}')
                for i in track(range(10), description="Downloading..."):
                    time.sleep(1)  # Simulate work being done
                stream = yt.streams.get_by_itag(22)
                stream.download()
            except:
                print('Conexion error')
                break
            print(GREEN + 'Success' + RESET)
            continue

        else:
            if resolution != '720' or resolution != '1080' or resolution != '360':
                print('Just 180,720,360 please!')
                continue
            else:
                resolution.isalpha()
                print('just numbers')
                continue

    elif choice == '2':
        print('Insert the video link')
        videoLink = str(input())
        yt = YouTube(f'{videoLink}')
        ys = yt.streams.filter(only_audio=True).first()
        ys.download()

    else:
        choice == '4' or choice == 'exit'
        print(RED + '▀▀█▀▀ █░░█ █▀▀█ █▀▀▄ █░█ █▀▀ 　 █▀▀ █▀▀█ █▀▀█ 　 █░░█ █▀▀ █▀▀ 　 █▀▄▀█ █▀▀█ █░█ ' + RESET)
        print(BLUE + '░░█░░ █▀▀█ █▄▄█ █░░█ █▀▄ ▀▀█ 　 █▀▀ █░░█ █▄▄▀ 　 █░░█ ▀▀█ █▀▀ 　 █░▀░█ █▄▄█ ▄▀▄ ' + RESET)
        print(GREEN + '░░▀░░ ▀░░▀ ▀░░▀ ▀░░▀ ▀░▀ ▀▀▀ 　 ▀░░ ▀▀▀▀ ▀░▀▀ 　 ░▀▀▀ ▀▀▀ ▀▀▀ 　 ▀░░░▀ ▀░░▀ ▀░▀ ' + RESET)
        print(GREEN + '█░░█ █▀▀█ █░░█ ▀▀█▀▀ █░░█ █▀▀▄ █▀▀ 　 █▀▀▄ █▀▀█ █░░░█ █▀▀▄ █░░ █▀▀█ █▀▀█ █▀▀▄ █▀▀ █▀▀█ ' + RESET)
        print(BLUE + '█▄▄█ █░░█ █░░█ ░░█░░ █░░█ █▀▀▄ █▀▀ 　 █░░█ █░░█ █▄█▄█ █░░█ █░░ █░░█ █▄▄█ █░░█ █▀▀ █▄▄▀ ' + RESET)
        print(RED + '▄▄▄█ ▀▀▀▀ ░▀▀▀ ░░▀░░ ░▀▀▀ ▀▀▀░ ▀▀▀ 　 ▀▀▀░ ▀▀▀▀ ░▀░▀░ ▀░░▀ ▀▀▀ ▀▀▀▀ ▀░░▀ ▀▀▀░ ▀▀▀ ▀░▀▀' + RESET)
        print('by.Rafael Guedes.')
        sleep(3)
        break
