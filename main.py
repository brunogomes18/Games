import pygame
pygame.init()

win = pygame.display.set_mode((800,800)) 

pygame.display.set_caption("Music Game")
run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            run = False
    
    pygame.draw.rect(win, (0, 255, 0), (0,0, 50, 50))
    pygame.display.update()

pygame.quit()
