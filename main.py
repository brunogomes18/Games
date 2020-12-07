import pygame
from random import randrange

pygame.init()
win = pygame.display.set_mode((800,800)) 
pygame.display.set_caption("Music Game")

soundR= pygame.mixer.Sound("sounds/sound1.wav")
soundT= pygame.mixer.Sound("sounds/sound2.wav")
soundY= pygame.mixer.Sound("sounds/sound3.wav")
soundU= pygame.mixer.Sound("sounds/sound4.wav")
soundF= pygame.mixer.Sound("sounds/sound5.wav")
soundG= pygame.mixer.Sound("sounds/sound6.wav")
soundH= pygame.mixer.Sound("sounds/sound7.wav")
soundC= pygame.mixer.Sound("sounds/sound8.wav")
soundV= pygame.mixer.Sound("sounds/sound9.wav")
soundB= pygame.mixer.Sound("sounds/sound10.wav")
soundN= pygame.mixer.Sound("sounds/sound11.wav")


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
textR = font.render('R ', 1, (255,255,255))
textList.append(textR)
textT = font.render('T ', 1, (255,255,255))
textList.append(textT)
textY = font.render('Y ', 1, (255,255,255))
textList.append(textY)
textU = font.render('U ', 1, (255,255,255))
textList.append(textU)

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
    pygame.draw.rect(win, (255,255,255), (x-10,y-10, 120, 120))
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
            if event.key == pygame.K_r:
                soundR.play()
            if event.key == pygame.K_t:
                soundT.play()
            if event.key == pygame.K_y:
                soundY.play()
            if event.key == pygame.K_u:
                soundU.play()
            if event.key == pygame.K_f:
                soundF.play()
            if event.key == pygame.K_g:
                soundG.play()
            if event.key == pygame.K_h:
                soundH.play()
            if event.key == pygame.K_c:
                soundC.play()
            if event.key == pygame.K_v:
                soundV.play()
            if event.key == pygame.K_b:
                soundB.play()
            if event.key == pygame.K_n:
                soundN.play()

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r:
                soundR.stop()
            if event.key == pygame.K_t:
                soundT.stop()
            if event.key == pygame.K_y:
                soundY.stop()
            if event.key == pygame.K_u:
                soundU.stop()
            if event.key == pygame.K_f:
                soundF.stop()
            if event.key == pygame.K_g:
                soundG.stop()
            if event.key == pygame.K_h:
                soundH.stop()
            if event.key == pygame.K_c:
                soundC.stop()
            if event.key == pygame.K_v:
                soundV.stop()
            if event.key == pygame.K_b:
                soundB.stop()
            if event.key == pygame.K_n:
                soundN.stop()

              


    pygame.display.update()

pygame.quit()
