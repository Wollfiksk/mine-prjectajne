import sys
import random
import pygame
pygame.init()

rozliseni_okna = (800, 600)

okno = pygame.display.set_mode(rozliseni_okna)

pozice_micku_x = 400
pozice_micku_y = 300
velikost_micku = 50
rychlost_micku_x = 0.5
rychlost_micku_y = 0.5

velikost_hrace_vyska = 120
velikost_hrace_sirka = 50


pozice_hrace_x = 10
pozice_hrace_y = 300
rychlost_hrace = 0.3

velikost_hrace_vyska2 = 120
velikost_hrace_sirka2 = 50


pozice_hrace_x2 = 740
pozice_hrace_y2 = 300
rychlost_hrace2 = 0.3



while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    stisknute_klavesy = pygame.key.get_pressed()
    
    if stisknute_klavesy[pygame.K_w]:
        pozice_hrace_y -= rychlost_hrace
        
    if stisknute_klavesy[pygame.K_s]:
        pozice_hrace_y += rychlost_hrace
        
    if stisknute_klavesy[pygame.K_UP]:
        pozice_hrace_y2 -= rychlost_hrace2
        
    if stisknute_klavesy[pygame.K_DOWN]:
        pozice_hrace_y2 += rychlost_hrace2
    
    
    pozice_micku_x += rychlost_micku_x
    pozice_micku_y += rychlost_micku_y
    
    if pozice_micku_x < 0:
        print("you lost")
        print("you lost")
        print("you lost")
        print("you lost")
        quit()
    if pozice_micku_y < 0:
        pozice_micku_y = 0
        rychlost_micku_y *= -1
        
    rand_pri_kol = random.randint(1, 2)
    
    hrac2_rect = pygame.Rect(pozice_hrace_x2, pozice_hrace_y2, velikost_hrace_sirka2, velikost_hrace_vyska2)
    hrac_rect = pygame.Rect(pozice_hrace_x, pozice_hrace_y, velikost_hrace_sirka, velikost_hrace_vyska)
    micek_rect = pygame.Rect(pozice_micku_x, pozice_micku_y, velikost_micku, velikost_micku)

    if hrac_rect.colliderect(micek_rect):
        rychlost_micku_x = abs(rychlost_micku_x)  
        if rand_pri_kol == 1:
            rychlost_micku_y *= -1.05
        if rand_pri_kol == 2:
            rychlost_micku_y *= 1.05

    if hrac2_rect.colliderect(micek_rect):
        rychlost_micku_x = -abs(rychlost_micku_x)  
        if rand_pri_kol == 1:
            rychlost_micku_y *= -1.05
        if rand_pri_kol == 2:
            rychlost_micku_y *= 1.05
    
    if pozice_micku_x > rozliseni_okna[0] - velikost_micku:
        print("you lost")
        print("you lost")
        print("you lost")
        print("you lost")
        quit()
    
    if pozice_micku_y > rozliseni_okna[1] - velikost_micku:
        pozice_micku_y = rozliseni_okna[1] - velikost_micku
        rychlost_micku_y *= -1
    
    okno.fill((255, 255, 255))
    
    pygame.draw.rect(okno, (0, 0, 0), (pozice_hrace_x, pozice_hrace_y, velikost_hrace_sirka,velikost_hrace_vyska))
    pygame.draw.ellipse(okno, (0, 0, 255), (pozice_micku_x, pozice_micku_y, velikost_micku, velikost_micku))
    pygame.draw.rect(okno, (0, 0, 0), (pozice_hrace_x2, pozice_hrace_y2, velikost_hrace_sirka2,velikost_hrace_vyska2))
    
    
    pygame.display.update()
