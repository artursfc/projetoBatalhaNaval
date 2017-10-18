# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:07:11 2017

@author: Artur Carneiro 31724833
"""



def inicializarGrid():
    x = 10
    y = 10
    
    matrix = [['.' for i in range(x)]for j in range(y)]
    return matrix

def posicionar_porta_avioes(grid,linha,coluna,vertical):
        size = 5
        if grid[linha][coluna] == '.':
            if vertical == True:
                 if linha > 5:
                    print('Inválido. Fora da grid')
                 elif check_pos_ver(grid,linha,coluna,size) == True:
                        for i in range(5):
                            grid[linha+i][coluna] = 'P'
#                        return print(pd.DataFrame(p))
                        return p
                 else:
                        print('Posição ocupada')
            elif vertical == False:
                if coluna > 5:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(5):
                            grid[linha][coluna+i] = 'P'
#                       return print(pd.DataFrame(p))
                        return p
                    else:
                        print('Posição ocupada')
        else:
            print('Posição ocupada')


def posicionar_encouracado(grid,linha,coluna,vertical):
        size = 4
        if grid[linha][coluna] == '.':
            if vertical == True:
                 if linha > 6:
                    print('Inválido. Fora da grid')
                 elif check_pos_ver(grid,linha,coluna,size) == True:
                        for i in range(4):
                            grid[linha+i][coluna] = 'E'
#                        return print(pd.DataFrame(p))
                        return p
                 else:
                        print('Posição ocupada')
            elif vertical == False:
                if coluna > 6:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(4):
                            grid[linha][coluna+i] = 'E'
#                        return print(pd.DataFrame(p))
                        return p
                    else:
                        print('Posição ocupada')
        else:
            print('Posição ocupada')
            
def posicionar_cruzador(grid,linha,coluna,vertical):
        size = 3
        if grid[linha][coluna] == '.':
            if vertical == True:
                 if linha > 7:
                    print('Inválido. Fora da grid')
                 elif check_pos_ver(grid,linha,coluna,size) == True:
                        for i in range(3):
                            grid[linha+i][coluna] = 'C'
#                        return print(pd.DataFrame(p))
                        return p
                 else:
                        print('Posição ocupada')
            elif vertical == False:
                if coluna > 7:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(3):
                            grid[linha][coluna+i] = 'C'
#                        return print(pd.DataFrame(p))
                        return p
                    else:
                        print('Posição ocupada')
        else:
            print('Posição ocupada')

def posicionar_sub(grid,linha,coluna,vertical):
        size = 2
        if grid[linha][coluna] == '.':
            if vertical == True:
                 if linha > 8:
                    print('Inválido. Fora da grid')
                 elif check_pos_ver(grid,linha,coluna,size) == True:
                        for i in range(2):
                            grid[linha+i][coluna] = 'S'
#                        return print(pd.DataFrame(p))
                        return p
                 else:
                        print('Posição ocupada')
            elif vertical == False:
                if coluna > 8:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(2):
                            grid[linha][coluna+i] = 'S'
#                        return print(pd.DataFrame(p))
                        return p
                    else:
                        print('Posição ocupada')
        else:
            print('Posição ocupada')

def check_pos_hor(grid,linha,coluna,size):
    cont = 0
    for l in range(size):
        if grid[linha][coluna+l] != '.':
            cont += 1
        else:
            cont += 0
    if cont != 0:
        return False
    else:
        return True

def check_pos_ver(grid,linha,coluna,size):
    cont = 0
    for l in range(size):
        if grid[linha+l][coluna] != '.':
            cont += 1
        else:
            cont += 0
    if cont != 0:
        return False
    else:
        return True

def imprimir_grid(grid):
     cabeçalho = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
     print(0 ,'', cabeçalho)
     cont = 1
     for i in grid:
         if cont == 10:
             print(cont,end=' ')
             print(i)
             break
         print(cont, end = "  ")
         print(i)
         cont += 1
     print('\n')

p = inicializarGrid()
imprimir_grid(p)
posicionar_porta_avioes(p,2,4,True)
posicionar_encouracado(p,4,6,False)
posicionar_cruzador(p,1,1,True)
posicionar_sub(p,9,1,False)
