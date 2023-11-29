import random
import pygame
import sys
from pygame.locals import *
# global varibales of game
FPS= 32
screenwidth=450
screenheight=800
screen= pygame.display.set_mode((screenwidth,screenheight))
groundy=screenheight*0.8
GAME_SPRITES={}
GAME_SOUNDS={}
PLAYER='bird.png'
BACKGROUND='bg.jpg'
PIPE='pipe.png'
MESSAGE='message.jpg'
BASE=50
# global functions starts here

def welcomeScreen():
    playerx=int(screenwidth/5)
    # playery=int((screenheight - GAME_SPRITES['player'].get_height())/2)
    playery=int(GAME_SPRITES['base'])
    messagex= int((screenwidth-GAME_SPRITES['message'].get_width())/2)
    messagey= int(screenheight*0.13)
    basex=0
    while True:
        for event in pygame.event.get():
            # if user click on cross button,close the
            if event.type==QUIT or (event.type==KEYDOWN and event.key== K_ESCAPE):
                pygame.quit()
                sys.exit()
                
            # if user press up and start the game
            elif event.type ==KEYDOWN and (event.key== K_SPACE or event.key==K_UP):
                return
            else:
                screen.blit(GAME_SPRITES['background'],(0,0))
                # screen.blit(GAME_SPRITES['pipe'][0],(0,(screenheight - GAME_SPRITES['pipe'][0].get_height())/2))
                screen.blit(GAME_SPRITES['player'],(playerx,playery))
                screen.blit(GAME_SPRITES['message'],(messagex,messagey))
                
                # screen.blit(GAME_SPRITES['base'],(basex, groundy))
                pygame.display.update()
                FPSCLOCK.tick(FPS)
def mainGame():
    score=0
    playerx= int(screenwidth/5)
    playery=int(screenwidth/2)
    basex= 0 
    
    #creating 2 pipes for blitting on the screen
    
    newPipe1=getRandomPipe() 
    newPipe2=getRandomPipe()
    
    # my list of upper pipes
    upperPipes=[
        {'x': screenwidth+200,'y':newPipe1[0]['y']},
        {'x': screenwidth+200+(screenwidth/2),'y':newPipe2[1]['y']},
    ]
    # my list of upper pipes
    lowerPipes=[
        {'x': screenwidth+200,'y':newPipe1[0]['y']},
        {'x': screenwidth+200+(screenwidth/2),'y':newPipe2[1]['y']},
    ]
    
    pipVelx= -4
    
    playervely=-9
    playermaxVelY=-10
    playerMinVelY=-8
    playerAccY=1
    
    
def getRandomPipe():
    # generating x and y of two pipes (on straight and one rotated)
    
    pipeHeight= GAME_SPRITES['pipe'][0].get_height()
    offset=screenheight/3
    # this is very crucial varible for the our game
    # it is defing the distance between two pipes, bird niklni bhi to chahiye
    
    y2= offset + random.randrange(0, int(screenheight-GAME_SPRITES['base'].get_height()-1.2*offset))
    pipeX=screenwidth+10
    
    y1= pipeHeight-y2 +offset
    pipe= [
        {'x':pipeX,'y': -y1},# upper pipe
        {'x':pipeX,'y': y2}# lower pipe
    ]
    return pipe
     
                
                                 
if __name__=="__main__":
    # execution of program starts
    pygame.init() #initailize the pygame's modules
    FPSCLOCK= pygame.time.Clock()
    pygame.display.set_caption("flappy bird game by Dhruvin")
    GAME_SPRITES['numbers']=(
        # pygame.image.load('0 image').convert_alpha(),
        # pygame.image.load('').convert_alpha(),
        # pygame.image.load('').convert_alpha(),
        # pygame.image.load('').convert_alpha(),
        # pygame.image.load('').convert_alpha(),
        # pygame.image.load('').convert_alpha(),
        # pygame.image.load('').convert_alpha(),
        # pygame.image.load('').convert_alpha(),
        # pygame.image.load('').convert_alpha(),
        # pygame.image.load('').convert_alpha(),
    )
    GAME_SPRITES['message']=pygame.image.load(MESSAGE).convert_alpha()
    # GAME_SPRITES['base']=pygame.image.load(BASE).convert_alpha()
    GAME_SPRITES['base']=screenheight-200
    GAME_SPRITES['pipe']=(
        pygame.transform.rotate(pygame.image.load(PIPE).convert_alpha() ,180),
        pygame.image.load(PIPE).convert_alpha()
    )
       
    # GAME_SPRITES['background']= pygame.transform.scale(,(200,200))
    GAME_SPRITES['background']= pygame.image.load(BACKGROUND).convert()
    GAME_SPRITES['player']= pygame.transform.scale(pygame.image.load(PLAYER).convert(),(100,100)) 
    
    while True:
        welcomeScreen() #show welcome screen for the user untill user start playing game
        