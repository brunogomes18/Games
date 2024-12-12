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

#my comment
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
                textList[0] = font.render('R ', 1, (255,0,0))
                soundR.play(5)
            if event.key == pygame.K_t:
                textList[1] = font.render('T ', 1, (255,0,0))
                soundT.play(5)
            if event.key == pygame.K_y:
                textList[2] = font.render('Y ', 1, (255,0,0))
                soundY.play(5)
            if event.key == pygame.K_u:
                textList[3] = font.render('U ', 1, (255,0,0))
                soundU.play(5)
            if event.key == pygame.K_f:
                textList[4] = font.render('F ', 1, (255,0,0))
                soundF.play(5)
            if event.key == pygame.K_g:
                textList[5] = font.render('G ', 1, (255,0,0))
                soundG.play(5)
            if event.key == pygame.K_h:
                textList[6] = font.render('H ', 1, (255,0,0))
                soundH.play(5)
            if event.key == pygame.K_c:
                textList[7] = font.render('C ', 1, (255,0,0))
                soundC.play(5)
            if event.key == pygame.K_v:
                textList[8] = font.render('V ', 1, (255,0,0))
                soundV.play(5)
            if event.key == pygame.K_b:
                textList[9] = font.render('B ', 1, (255,0,0))
                soundB.play(5)
            if event.key == pygame.K_n:
                textList[10] = font.render('N ', 1, (255,0,0))
                soundN.play(5)

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_r: 
                textList[0] = font.render('R ', 1, (255,255,255))
                soundR.stop()
            if event.key == pygame.K_t:
                textList[1] = font.render('T ', 1, (255,255,255))
                soundT.stop()
            if event.key == pygame.K_y:
                textList[2] = font.render('Y ', 1, (255,255,255))
                soundY.stop()
            if event.key == pygame.K_u:
                textList[3] = font.render('U ', 1, (255,255,255))
                soundU.stop()
            if event.key == pygame.K_f:
                textList[4] = font.render('F ', 1, (255,255,255))
                soundF.stop()
            if event.key == pygame.K_g:
                textList[5] = font.render('G ', 1, (255,255,255))
                soundG.stop()
            if event.key == pygame.K_h:
                textList[6] = font.render('H ', 1, (255,255,255))
                soundH.stop()
            if event.key == pygame.K_c:
                textList[7] = font.render('C ', 1, (255,255,255))
                soundC.stop()
            if event.key == pygame.K_v:
                textList[8] = font.render('V ', 1, (255,255,255))
                soundV.stop()
            if event.key == pygame.K_b:
                textList[9] = font.render('B ', 1, (255,255,255))
                soundB.stop()
            if event.key == pygame.K_n:
                textList[10] = font.render('N ', 1, (255,255,255))
                soundN.stop()
    x= 50
    y= 100
    i=0
    
    while i<11:
        text = textList[i]
        win.blit(text, (x+20, y+20)) 
        x+=200
        i+=1
        if x > 700:   
            x = x%700
            y+=200      


    pygame.display.update()

pygame.quit()
