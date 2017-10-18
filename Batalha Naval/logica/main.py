# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:07:11 2017

@author: Artur Carneiro 31724833
"""

import pandas as pd



def inicializarGrid():
    x = 10
    y = 10
    
    matrix = [['.' for i in range(x)]for j in range(y)]
    return matrix

def posicionar_porta_avioes(grid,linha,coluna,vertical):
        if grid[linha][coluna] == '.':
            if vertical == True:
                 if linha > 5:
                    print('Inválido. Fora da grid')
                 elif check_pos_ver(grid,linha,coluna) == True:
                        for i in range(5):
                            grid[linha+i][coluna] = 'P'
                        return print(pd.DataFrame(p))
#                           return imprimir_grid(p)
                 else:
                        print('Posição ocupada')
            elif vertical == False:
                if coluna > 5:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna) == True:
                        for i in range(5):
                            grid[linha][coluna+i] = 'P'
                        return print(pd.DataFrame(p))
#                           return imprimir_grid(p)
                    else:
                        print('Posição ocupada')
        else:
            print('Posição ocupada')


p = inicializarGrid()

def check_pos_hor(grid,linha,coluna):
    cont = 0
    for l in range(5):
        if grid[linha][coluna+l] != '.':
            cont += 0
        else:
            cont += 1
    if cont != 0:
        return True
    else:
        return False

def check_pos_ver(grid,linha,coluna):
    cont = 0
    for l in range(5):
        if grid[linha+l][coluna] != '.':
            cont += 0
        else:
            cont += 1
    if cont != 0:
        return True
    else:
        return False

#def imprimir_grid(grid):
#     cabeçalho = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#     print(0 ,'', cabeçalho)
#     cont = 1
#     for i in grid:
#         if cont == 10:
#             print(cont,end=' ')
#             print(i)
#             break
#         print(cont, end = "  ")
#         print(i)
#         cont += 1





