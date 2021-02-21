from random import *
import pygame
import time
def aff_tab():
    for i in range(y):
        for j in range(x):
            print(tab[i][j], end=" ")
        print()

def remplir_tab(tab):
    for i in range(y):
        for j in range(x):
            if tab[i][j]==0:
                tab[i][j]=randint(1,nb_color)

def verif_tab(tab):
    #Verif ligne pour 3
    for i in range(y):
        for j in range(x-2):
            if tab[i][j]==tab[i][j+1] and tab[i][j]==tab[i][j+2]:
                tab[i][j], tab[i][j+1], tab[i][j+2] = 0, 0, 0
                
    #Verif colone pour 3
    for i in range(y-2):
        for j in range(x):
            if tab[i][j]==tab[i+1][j] and tab[i][j]==tab[i+2][j]:
                tab[i][j], tab[i+1][j], tab[i+2][j] = 0, 0, 0
                


def monter(tab):
    for i in range(x):
        liste=[]
        compteur=0
        for j in range(y):
            if tab[j][i]!=0:
                liste.append(tab[j][i])
        for j in range(y):
            if j<y-len(liste):
                tab[j][i]=0
            else:
                tab[j][i]=liste[compteur]
                compteur+=1

def joue(tab, x, y, x1, y1):
    #Manque une vérification
    var=tab[x][y]
    tab[x][y]=tab[x1][y1]
    tab[x1][y1]=var

def init(tab):
    for i in range(len(tab)):
        fruits.append(pygame.image.load("assets/"+tab[i]+".png"))
        fruits[len(fruits)-1].convert_alpha()
        fruits[len(fruits)-1] = pygame.transform.scale(fruits[len(fruits)-1], [ratio, ratio])



resolution_x=1280
resolution_y=720
pos1=(0,0)
pos2=(0,0)   

x=12
y=7
nb_color=5
tab=[0]*y
for i in range(len(tab)):
    tab[i]=[0]*x
remplir_tab(tab)

pygame.init()
window_surface=pygame.display.set_mode((resolution_x, resolution_y))

if resolution_x>resolution_y:
    if x > y:
        ratio = resolution_y//y
    else:
        ratio = resolution_y//x
else:
    if x > y:
        ratio = resolution_x//y
    else:
        ratio = resolution_x//x


#Initialisation de couleur
black_color=(20,20,20)

#Initialisation des 6 fruits
fruits=[]
init(["fruit1","fruit2","fruit3","fruit4","fruit5","fruit6"])
cadre = pygame.image.load("assets/cadre.png")
fond = pygame.image.load("assets/fond.jpg")
rect= pygame.Surface((ratio,ratio))
rect.set_alpha(180)
rect.fill((17, 70, 105))
#convert alpha
cadre.convert_alpha()
#Adaptation de la taille
fond = pygame.transform.scale(fond, [resolution_x, resolution_y])
cadre = pygame.transform.scale(cadre, [ratio, ratio])

launched=True
while launched:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            launched=False
        else:
            #window_surface.fill(black_color)
            window_surface.blit(fond, [0, 0])
            for i in range(y):
                for j in range(x):  
                    window_surface.blit(rect, (ratio*j, ratio*i))              
                    window_surface.blit(fruits[tab[i][j]-1], [ratio*j, ratio*i])
                    window_surface.blit(fruits[tab[i][j]-1], [ratio*j, ratio*i])
                    #pygame.draw.line(window_surface, (200, 200, 200), (0, ratio*i), (resolution_x, ratio*i))
                    #pygame.draw.line(window_surface, (200, 200, 200), (ratio*j, 0), (ratio*j, resolution_y))

        if event.type == pygame.MOUSEBUTTONDOWN:
            pos1 = pygame.mouse.get_pos()    

        if event.type == pygame.MOUSEBUTTONUP:
            pos2 = pygame.mouse.get_pos()
        
        if pos1!=(0,0):
            window_surface.blit(cadre, [ratio*(pos1[0]//ratio), ratio*(pos1[1]//ratio)])

        if pos1!=(0,0) and pos2!=(0,0):
            if (pos1[0]//ratio==pos2[0]//ratio and (pos1[1]//ratio==pos2[1]//ratio+1 or pos1[1]//ratio==pos2[1]//ratio-1)) or (pos1[1]//ratio==pos2[1]//ratio and (pos1[0]//ratio==pos2[0]//ratio+1 or pos1[0]//ratio==pos2[0]//ratio-1)):
                joue(tab, pos1[1]//ratio, pos1[0]//ratio, pos2[1]//ratio, pos2[0]//ratio)
            #print(pos1[0]//ratio, pos1[1]//ratio, pos2[0]//ratio, pos2[1]//ratio)
            pos1=(0,0)
            pos2=(0,0)
        verif_tab(tab)
        monter(tab)
        remplir_tab(tab)
    pygame.display.flip()
