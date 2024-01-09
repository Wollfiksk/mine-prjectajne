import sys

import pygame
pygame.init()

rozliseni_okna = (800, 600)

okno = pygame.display.set_mode(rozliseni_okna)

pozice_micku_x = 300
pozice_micku_y = 200
velikost_micku = 50
rychlost_micku_x = 0.5
rychlost_micku_y = 0.5

pozice_hrace_x = 10
pozice_hrace_y = 10
rychlost_hrace = 0.3

while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    stisknute_klavesy = pygame.key.get_pressed()
    
    if stisknute_klavesy[pygame.K_UP]:
        pozice_hrace_y -= rychlost_hrace
        
    if stisknute_klavesy[pygame.K_DOWN]:
        pozice_hrace_y += rychlost_hrace
    
    
    pozice_micku_x += rychlost_micku_x
    pozice_micku_y += rychlost_micku_y
    
    if pozice_micku_x < 0:
        pozice_micku_x = 0
        rychlost_micku_x *= -1
    if pozice_micku_y < 0:
        pozice_micku_y = 0
        rychlost_micku_y *= -1
    
    if pozice_micku_x > rozliseni_okna[0] - velikost_micku:
        pozice_micku_x = rozliseni_okna[0] - velikost_micku
        rychlost_micku_x *= -1
    if pozice_micku_y > rozliseni_okna[1] - velikost_micku:
        pozice_micku_y = rozliseni_okna[1] - velikost_micku
        rychlost_micku_y *= -1
    
    okno.fill((255, 255, 255))
    
    pygame.draw.rect(okno, (0, 0, 0), (pozice_hrace_x, pozice_hrace_y, 50,120))
    pygame.draw.ellipse(okno, (0, 0, 255), (pozice_micku_x, pozice_micku_y, velikost_micku, velikost_micku))
    
    pygame.display.update()
