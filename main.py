import pygame

pygame.init()
win = pygame.display.set_mode((800,800)) 
pygame.display.set_caption("Music Game")

soundE= pygame.mixer.Sound("sounds/sound1.wav")
soundR= pygame.mixer.Sound("sounds/sound2.wav")


run = True
x= 50
y= 100
r=20
g=20
b=20

#draw init
win.fill((0,0,0))

i=0
while i<11:
    pygame.draw.rect(win, (r,g,b), (x,y, 100, 100))
    i+=1
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
