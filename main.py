import pygame
from random import randrange

pygame.init()
win = pygame.display.set_mode((800,800)) 
pygame.display.set_caption("Music Game")

soundE= pygame.mixer.Sound("sounds/sound1.wav")
soundR= pygame.mixer.Sound("sounds/sound2.wav")


run = True
x= 50
y= 100
r=0
g=250
b=0

#draw init
win.fill((0,0,0))
textList = []

font = pygame.font.SysFont('comicsans', 100)
textE = font.render('E ', 1, (255,255,255))
textList.append(textE)
textR = font.render('R ', 1, (255,255,255))
textList.append(textR)
textT = font.render('T ', 1, (255,255,255))
textList.append(textT)
textY = font.render('Y ', 1, (255,255,255))
textList.append(textY)

textF = font.render('F ', 1, (255,255,255))
textList.append(textF)
textG = font.render('G ', 1, (255,255,255))
textList.append(textG)
textH = font.render('H ', 1, (255,255,255))
textList.append(textH)

textC = font.render('C ', 1, (255,255,255))
textList.append(textC)
textV = font.render('V ', 1, (255,255,255))
textList.append(textV)
textB = font.render('B ', 1, (255,255,255))
textList.append(textB)
textN = font.render('N ', 1, (255,255,255))
textList.append(textN)


i=0
while i<11:
    pygame.draw.rect(win, (r,g,b), (x,y, 100, 100))
    text = textList[i]
    win.blit(text, (x+20, y+20))
    i+=1
    r=randrange(255)
    g=randrange(255)
    b=randrange(255)
    x+=200
    if x > 700:   
        x = x%700
        y+=200
    



# Main Loop
while run:
    pygame.time.delay(100)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                soundE.play()
            if event.key == pygame.K_r:
                soundR.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_e:
                soundE.stop()
            if event.key == pygame.K_r:
                soundR.stop()

              


    pygame.display.update()

pygame.quit()
