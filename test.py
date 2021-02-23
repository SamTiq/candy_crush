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
        return()
    if verif_tab(tab,4):
        print(4444)
        return()
    if verif_tab(tab,3):
        print(3333)
        return()


def aff_tab():
    for i in range(y):
        for j in range(x):
            print(tab[i][j], end=" ")
        print()


tab = [[2, 3, 4, 1, 1, 0, 1, 2, 2, 2, 2, 3], [2, 1, 4, 5, 1, 5, 5, 5, 3, 4, 5, 5], [2, 3, 4, 4, 5, 5, 1, 2, 5, 3, 2, 5], [2, 5, 3, 5, 5, 4, 5, 1, 3, 5, 5, 2], [4, 3, 2, 3, 4, 1, 2, 3, 4, 4, 3, 1], [4, 1, 1, 4, 3, 5, 1, 4, 3, 1, 4, 1], [3, 1, 1, 1, 1, 3, 2, 4, 4, 2, 5, 1]]
x=12
y=7
aff_tab()
print()
verif_total(tab)
aff_tab()



'''
def verif_tab(tab):
    #Verif ligne pour 3
    for i in range(y):
        for j in range(x-2):
            if tab[i][j]==tab[i][j+1] and tab[i][j]==tab[i][j+2]:
                tab[i][j], tab[i][j+1], tab[i][j+2] = 0, 0, 0
                return True
                
    #Verif colone pour 3
    for i in range(y-2):
        for j in range(x):
            if tab[i][j]==tab[i+1][j] and tab[i][j]==tab[i+2][j]:
                tab[i][j], tab[i+1][j], tab[i+2][j] = 0, 0, 0
                return True
    
    return False
'''