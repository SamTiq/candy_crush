from random import *
import pygame

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

def verif_tab(tab, nb):
    #Verif ligne pour nb
    compteur=0
    for i in range(y):
        for j in range(x-nb+1):
            for k in range(1, nb):
                if tab[i][j]==tab[i][j+k]:
                    compteur+=1
            if compteur==nb-1:
                for k in range(nb):
                    tab[i][j+k]=0
                return True
            compteur=0

                
    #Verif colone pour nb
    
    for i in range(y-nb+1):
        for j in range(x):
            for k in range(1, nb):
                if tab[i][j]==tab[i+k][j]:
                    compteur+=1
            if compteur==nb-1:
                for k in range(nb):
                    tab[i+k][j] = 0
                return True
            compteur=0
    return False

def verif_total(tab):
    if verif_tab(tab,5):
        print(5555)
        return True
    if verif_tab(tab,4):
        print(4444)
        return True
    if verif_tab(tab,3):
        print(3333)
        return True
    return False

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

def rezi(fond, cadre, rect):
    for i in range(len(tab)):
        fruits[len(fruits)-1] = pygame.transform.scale(fruits[len(fruits)-1], [ratio, ratio])

    fond = pygame.transform.scale(fond, [resolution_x, resolution_y])
    cadre = pygame.transform.scale(cadre, [ratio, ratio])
    rect= pygame.Surface((ratio,ratio))
    rect.set_alpha(180)
    rect.fill((17, 70, 105))



resolution_x=1280
resolution_y=720
pos1=(0,0)
pos2=(0,0)   

x=10
y=10
nb_color=6
tab=[0]*y
for i in range(len(tab)):
    tab[i]=[0]*x
remplir_tab(tab)
pygame.init()
window_surface=pygame.display.set_mode((resolution_x, resolution_y),pygame.RESIZABLE)

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
        
        elif event.type == pygame.VIDEORESIZE:
            resolution_x=window_surface.get_width()
            resolution_y=window_surface.get_height()

            if resolution_x/x>resolution_y/y:
                if x > y:
                    ratio = resolution_y//y
                else:
                    ratio = resolution_y//x
            else:
                if x > y:
                    ratio = resolution_x//y
                else:
                    ratio = resolution_x//x
            
            rezi(fond, cadre, rect)
        else:
            window_surface.fill(black_color)
            window_surface.blit(fond, [0, 0])
            for i in range(y):
                for j in range(x):
                    if tab[i][j]!=-1:  
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
        if verif_tab(tab,3):
            monter(tab)
            remplir_tab(tab)

    pygame.display.flip()
