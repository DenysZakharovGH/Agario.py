import pygame
import random  
import time 


FPS = 30
W = 1800  # ширина экрана
H = 1000  # высота экрана
WHITE =     (255,   255,    255)


BLUE =      (0,     70,     225)
WHITE =     (255,   255,    255)
RED =       (225,   0,      50)
GREEN =     (0,     225,    0)
Aqua =	 	   (0,	 	  128	, 	 128)
Navy_Blue =	(0,	 	  0,	 	   128)
Orange	= 	  (255,	  165,	   0)
Yellow	 =	  (255,	  255, 	  0)

list_of_colors = [BLUE,RED,GREEN,Aqua,Navy_Blue,Orange,Yellow]

pygame.init()
sc = pygame.display.set_mode((W, H))
clock = pygame.time.Clock()
 
# координаты и радиус круга
x = W // 2
y = H // 2
r = 10
 
motion = STOP

list_of_circles = []
for i in range(100):
    list_of_circles.append([random.randrange(0,W,2),random.randrange(0,H,2),random.choice(list_of_colors)])
    

x1 =0 
y1 =0
speed = 4
 
font = pygame.font.Font(pygame.font.get_default_font(), 36)
text_start= font.render('Сьешь все и не попадись ЗЕЛЕНОМУ', True, (0, 0, 0))
text_finish= font.render('ТЫ ПОБЕДИЛ', True, (0, 0, 0))
text_lose= font.render('ТЫ ПРОИГРАЛ', True, (0, 0, 0))


while 1:
    sc.fill(WHITE) # заливаем фон
    sc.blit(text_start, dest=(800,800))
    for i in list_of_circles:
        pygame.draw.circle(sc, i[-1], (i[0:2]), 10)

    pygame.draw.circle(sc, BLUE, (int(x), int(y)), int(r)) # рисуем круг

    pygame.draw.circle(sc, GREEN, (x1, y1), r)


    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            pygame.quit()
    # ----------------------for use --------------------------
    if pygame.mouse.get_focused():
        pos = pygame.mouse.get_pos()
    # ----------------------for use --------------------------
    #let our circle go to the 100,100

    try:
        if x > i.pos[0]:
            x-=speed
        if x < i.pos[0]:
            x+=speed
        if y > i.pos[1]:
            y-=speed
        if y < i.pos[1]:
            y+=speed
    except :
        pass

    if x1 > x:
            x1-=2
    if x1 < x:
            x1+=2
    if y1 > y:
            y1-=2
    if y1 < y:
            y1+=2
    
    

    for i in list_of_circles:
        #i[0:2]
        if (i[0]-x)**2 + (i[1]-y)**2 <= r**2:
            list_of_circles.remove(i)
            r+=1
            speed -= 0.01


    if (x - x1)**2 + (y - y1)**2 <= r**2:
            sc.blit(text_lose, dest=(800,800))
            time.sleep(5)
        
    if len(list_of_circles) == 0:
        sc.blit(text_finish, dest=(800,800))
        time.sleep(5)


            

    pygame.display.update()
 
    clock.tick(FPS)



