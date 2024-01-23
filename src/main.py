import sys
import random
import pygame
import time


pygame.init()
pygame.font.init()

rozliseni_okna = (800, 600)

okno = pygame.display.set_mode(rozliseni_okna)
soubor = open("G:\Python\mine-prjectajne\save\Save.txt", 'r', encoding = 'utf-8')

for jeden_radek in soubor:
    skorestr = jeden_radek
    skore = int(skorestr)
        

soubor.close()

randoms = random.randint(50,500)
pozice_micku_y = randoms
pozice_micku_x = 400
velikost_micku = 50
randoms2 = random.randint(1,2)
if randoms2 == 1:
    rychlost_micku_x = 0.3
if randoms2 == 2:
    rychlost_micku_x = -0.3
rychlost_micku_y = 0.3

velikost_hrace_vyska = 150
velikost_hrace_sirka = 50

pozice_hrace_x = 10
pozice_hrace_y = 300
rychlost_hrace = 0.6

velikost_hrace_vyska2 = 150
velikost_hrace_sirka2 = 50

clock = pygame.time.Clock()

pozice_hrace_x2 = 740
pozice_hrace_y2 = 300
rychlost_hrace2 = 0.6

button_rect2 = pygame.Rect(300, 200, 200, 100)
button_rect = pygame.Rect(300, 330, 200, 100)
button_color = (100, 100, 100)
click_color = (100, 100, 100)

font = pygame.font.SysFont(None , 40)
font2 = pygame.font.SysFont(None , 40)
esc = False

jo = False
jo2 = False 
fps = str(int(clock.get_fps()))

def draw_button(rect, color, text):
    pygame.draw.rect(okno, color, rect)
    text_surface = font.render(text, True, (255, 255, 255))
    text_rect = text_surface.get_rect(center=rect.center)
    okno.blit(text_surface, text_rect)
    
def draw_text(x, y):
    txtimg = font2.render("Skore: " + str(skore), True, (0, 0, 0))
    okno.blit(txtimg, (x, y))

def fps_counter():
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    okno.blit(fps_t,(0,0))

def reset_game():
    global pozice_micku_x, pozice_micku_y, skore
    pozice_micku_x = 400
    pozice_micku_y = 300
    skore = 0
    
while True:
    for udalost in pygame.event.get():
        if udalost.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif udalost.type == pygame.KEYDOWN:
            if udalost.key == pygame.K_ESCAPE:
                esc = not esc
        elif udalost.type == pygame.MOUSEBUTTONDOWN:
            if udalost.button == 1:
                if button_rect.collidepoint(udalost.pos):
                    print("reset")
                    reset_game()
        elif udalost.type == pygame.MOUSEBUTTONDOWN:
            if udalost.button == 1:
                if button_rect2.collidepoint(udalost.pos):
                    print("Quited")
                    quit()
        
    
    if esc:
        is_hovered = button_rect.collidepoint(pygame.mouse.get_pos())
        is_hovered2 = button_rect2.collidepoint(pygame.mouse.get_pos())
        
        pygame.draw.rect(okno, (0, 0, 0), (100, 100, 600, 400))
        if is_hovered:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
                draw_button(button_rect, click_color, "Reseted")
            else:
                wsdraw_button(button_rect, button_color, "Reset")
        else:
            draw_button(button_rect, button_color, "Reset")

        if is_hovered2:
            if pygame.mouse.get_pressed()[0]:  # Left mouse button is pressed
                draw_button(button_rect2, click_color, "Quited and Saved")
                soubor2 = open("G:\Python\mine-prjectajne\save\Save.txt", 'w', encoding = 'utf-8')
                soubor2.write(str(skore))
                soubor2.close()
                
                quit()
            else:
                draw_button(button_rect2, button_color, "Quit and Save")
        else:
            draw_button(button_rect2, button_color, "Quit and Save")
            
        pygame.display.flip()
        
        
    
    if not esc:            
        stisknute_klavesy = pygame.key.get_pressed()
        
        
        okno.fill((255, 255, 255))
        if skore > -1 and skore < 10:
            draw_text(690, 0)
        if skore > 9 and skore < 99:
            draw_text(675, 0)
        if skore > 98:
            draw_text(650, 0)
        
        fps_counter()
        clock.tick()
        hrac2_rect = pygame.Rect(pozice_hrace_x2, pozice_hrace_y2, velikost_hrace_sirka2, velikost_hrace_vyska2)
        hrac_rect = pygame.Rect(pozice_hrace_x, pozice_hrace_y, velikost_hrace_sirka, velikost_hrace_vyska)
        micek_rect = pygame.Rect(pozice_micku_x, pozice_micku_y, velikost_micku, velikost_micku)
        
        
        if stisknute_klavesy[pygame.K_w]:
            if pozice_hrace_y > 0:
                pozice_hrace_y -= rychlost_hrace
            if hrac_rect.colliderect(micek_rect):
                if jo:
                    rychlost_micku_x = abs(rychlost_micku_x)
                    rychlost_micku_y -= rychlost_hrace * 0.5
                    jo = False
            
        if stisknute_klavesy[pygame.K_s]:
            if pozice_hrace_y < (rozliseni_okna[1] - velikost_hrace_vyska):
                pozice_hrace_y += rychlost_hrace
            if hrac_rect.colliderect(micek_rect):
                if jo:
                    rychlost_micku_x = abs(rychlost_micku_x)
                    rychlost_micku_y += rychlost_hrace * 0.5
                    jo = False
                    
        if stisknute_klavesy[pygame.K_UP]:
            if pozice_hrace_y2 > 0:
                pozice_hrace_y2 -= rychlost_hrace2 
            if hrac2_rect.colliderect(micek_rect):
                if jo2:
                    rychlost_micku_x = abs(rychlost_micku_x)
                    rychlost_micku_y -= rychlost_hrace2 * 0.5
                    jo2 = False
                    
        if stisknute_klavesy[pygame.K_DOWN]:
            if pozice_hrace_y2 < (rozliseni_okna[1] - velikost_hrace_vyska2):
                pozice_hrace_y2 += rychlost_hrace2
            if hrac2_rect.colliderect(micek_rect):
                if jo2:
                    rychlost_micku_x = abs(rychlost_micku_x)
                    rychlost_micku_y += rychlost_hrace2 * 0.5
                    jo2 = False
                    
                    
        pozice_micku_x += rychlost_micku_x
        pozice_micku_y += rychlost_micku_y
        
        rand_pri_kol = random.randint(1, 2)
       
        if hrac_rect.colliderect(micek_rect):
            if jo:
                if not stisknute_klavesy[pygame.K_w] or stisknute_klavesy[pygame.K_s]:
                    rychlost_micku_x = abs(rychlost_micku_x)
                    skore += 1
                    if rand_pri_kol == 1:
                        rychlost_micku_y *= -1
                    if rand_pri_kol == 2:
                        rychlost_micku_y *= 1
                    jo = False
            
        if hrac2_rect.colliderect(micek_rect):
            if jo2:
                if not stisknute_klavesy[pygame.K_DOWN] or stisknute_klavesy[pygame.K_UP]:
                    rychlost_micku_x = -abs(rychlost_micku_x)
                    skore += 1
                    if rand_pri_kol == 1:
                        rychlost_micku_y *= -1
                    if rand_pri_kol == 2:
                        rychlost_micku_y *= 1
                    jo2 = False
                
        if not hrac2_rect.colliderect(micek_rect):
            jo2 = True
            
        if not hrac_rect.colliderect(micek_rect):
            jo = True
            
        
        if pozice_micku_x < 0:
            print("you lost")
            print("you lost")
            print("you lost")
            print("you lost")
            soubor2 = open("G:\Python\mine-prjectajne\save\Save.txt", 'w', encoding = 'utf-8')
            soubor2.write(str(0))
            soubor2.close()
            quit()
            
        if pozice_micku_y < 0:
            pozice_micku_y = 0
            rychlost_micku_y *= -1
            
        
        if pozice_micku_x > rozliseni_okna[0] - velikost_micku:
            print("you lost")
            print("you lost")
            print("you lost")
            print("you lost")
            soubor2 = open("G:\Python\mine-prjectajne\save\Save.txt", 'w', encoding = 'utf-8')
            soubor2.write(str(0))
            soubor2.close()
            quit()

        if pozice_micku_y > rozliseni_okna[1] - velikost_micku:
            pozice_micku_y = rozliseni_okna[1] - velikost_micku
            rychlost_micku_y *= -1
        
        pygame.draw.rect(okno, (0, 0, 0), (pozice_hrace_x, pozice_hrace_y, velikost_hrace_sirka, velikost_hrace_vyska))
        pygame.draw.ellipse(okno, (0, 0, 255), (pozice_micku_x, pozice_micku_y, velikost_micku, velikost_micku))
        pygame.draw.rect(okno, (0, 0, 0), (pozice_hrace_x2, pozice_hrace_y2, velikost_hrace_sirka2, velikost_hrace_vyska2))

        
        
        pygame.display.update()
