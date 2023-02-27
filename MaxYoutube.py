# Rafael guedes
# github.com/guedes2142
from pytube import YouTube
from time import sleep
from rich.progress import track
import os
from colorama import Fore, Style
import pygame
from pygame.locals import *
from musictheme import *
import pyttsx3
# colors
RED = "\033[1;31m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD = "\033[;1m"
REVERSE = "\033[;7m"

engine = pyttsx3.init()



#Background music
playsound()
# path
# SAVE_PATH = 'C:/Users/Rafael/Desktop'
# banner
text = 'Thanks for use'
print(CYAN + f'{text:*^88}' + RESET)
print()
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
print(Fore.YELLOW + 'Downloading copyrighted YouTube videos is illegal!\n'
'I am not responsible for your downloads! Go at your own risk!' + Style.RESET_ALL)

while True:

    print(GREEN + 'Note:The file will be saved in the same folder as this app ' + RESET)
    print(BLUE + '****************************************************************************************' + RESET)
    # options
    print(RED + f'Choose an option' + RESET)
    print(Fore.GREEN + '1 >> Download video' + Style.RESET_ALL)
    print(Fore.LIGHTGREEN_EX + '2 >> Only audio.mp4 ' + Style.RESET_ALL)
    print(Fore.BLUE + '3 >> Search' + Style.RESET_ALL)
    print(Fore.LIGHTBLUE_EX + '4 >> exit' + Style.RESET_ALL)
    print(Fore.LIGHTRED_EX + '5 >> Stop music' + Style.RESET_ALL)
    print()
    choice = input('')

    if choice == '1':
        print(Fore.LIGHTCYAN_EX + 'Choose a resolution [1080],[720],[360] ' + Style.RESET_ALL)
        resolution = input()

        if resolution == '1080':
            try:
                print(GREEN + 'Insert the video link' + RESET)
                videoLink = str(input(''))
                yt = YouTube(f'{videoLink}')
                print('You are downloading>> ',yt.title)
                for i in track(range(10), description="Downloading..."):
                    sleep(1)  # Simulate work being done
                    stream = yt.streams.get_by_itag(137)
                    stream.download()
            except:
                print('Error! checkout you conection,or please try 720 360 px')
                print('Maybe you video dont have some resolutions')
                
                break
            print(GREEN + 'Success' + RESET)
            leia = engine.say('Download from youtube was completed successfully')
            engine.runAndWait()
            continue

        elif resolution == '720':
            
            try:
                print(GREEN + 'Insert the video link' + RESET)
                videoLink = str(input(''))
                
                yt = YouTube(f'{videoLink}')
                
                print('You are downloading>> ',yt.title)
                for i in track(range(10), description="Downloading..."):
                    sleep(1) 
                    print('Please wait===================*')
                    
                    stream = yt.streams.get_by_itag(22)
                    stream.download()
            except:
                print(Fore.YELLOW + 'Error checkout you conection,or please try 360 px' )
                print('Maybe you video dont have some resolutions')
                print("if don't work yet please contact me, or made me pull request on GitHub" + Style.RESET_ALL)
                break
            print(GREEN + 'Success' + RESET)
            leia = engine.say('Download from youtube was completed successfully')
            engine.runAndWait()
            continue

        elif resolution == '360':
            try:
                print(GREEN + 'Insert the video link' + RESET)
                videoLink = str(input(''))
                yt = YouTube(f'{videoLink}')
                print('You are downloading>> ',yt.title)
                for i in track(range(10), description="Downloading..."):
                    sleep(1)
                    print('Please wait===================*')

                    stream = yt.streams.get_by_itag(18)
                    stream.download()
            except Exception() as e:
                print('The following erro happend',e)
                print("if don't work yet please contact me, or made me pull request on GitHub" + Style.RESET_ALL)
            
            print(GREEN + 'Success' + RESET)
            leia = engine.say('Download from youtube was completed successfully')
            engine.runAndWait()
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
        videoLink = str(input(''))
        yt = YouTube(f'{videoLink}')
        ys = yt.streams.filter(only_audio=True).first()
        ys.download()
        
    elif choice == '5':
        stopSong()

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
