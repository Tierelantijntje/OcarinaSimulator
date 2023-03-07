import sys, termios, tty, pygame
pygame.mixer.init()

#This is pretty much the first program I've ever made, so don't expect too much. I only found files for the five base notes, If I ever find more for the sharps and flats, I'll add them.
#Sounds are supplied by HelpTheWretched, over on https://www.zeldasounds.com, alternately you can download a zip with all OoT instrument sounds from https://www.noproblo.dayjo.org/ZeldaSounds/OOT/OOT_Notes.zip 
#For the tabs of the in-game songs, go to https://www.zeldadungeon.net/wiki/Ocarina_of_Time_Songs or https://www.zeldadungeon.net/wiki/Majora%27s_Mask_Songs 

#If you are having problems, make sure you've installed Pygame, and your path for the .wav files is set correctly.


# Code to detect your keyboard press
def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch

#Ocarina note functions:
ocarinaD = pygame.mixer.Sound("./OcarinaSimulator/OOT_Notes_Ocarina_D_med.wav")
ocarinaF = pygame.mixer.Sound("./OcarinaSimulator/OOT_Notes_Ocarina_F_med.wav") 
ocarinaA = pygame.mixer.Sound("./OcarinaSimulator/OOT_Notes_Ocarina_A_med.wav")
ocarinaB = pygame.mixer.Sound("./OcarinaSimulator/OOT_Notes_Ocarina_B_med.wav")
ocarinaD2 = pygame.mixer.Sound("./OcarinaSimulator/OOT_Notes_Ocarina_D2_med.wav")  

#Main loop:
while True:
    # char is your input. By default the five notes are set to 0, 2, 4, 6, and 8.
    # To transcribe From the N64 input to keyboard numpad: A = 0, CDown = 2, CLeft = 4, CRight = 6, CUp = 8.
    char = getch()
    if char == "0":
        print("D")
        pygame.mixer.fadeout(250)
        pygame.mixer.Sound.play(ocarinaD)
    if char == "2": 
        print("F")
        pygame.mixer.fadeout(250)
        pygame.mixer.Sound.play(ocarinaF)
    if char == "6": 
        print("A")
        pygame.mixer.fadeout(250)
        pygame.mixer.Sound.play(ocarinaA)
    if char == "4": 
        print("B")
        pygame.mixer.fadeout(250)
        pygame.mixer.Sound.play(ocarinaB)
    if char == "8": 
        print("D8a")
        pygame.mixer.fadeout(250)
        pygame.mixer.Sound.play(ocarinaD2)  
