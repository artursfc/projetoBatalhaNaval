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
                print('ERROR 0031321.bnb2.x0y77')
            else:
                for i in range(5):
                    grid[linha+i][coluna] = 'P'
                return print(pd.DataFrame(p))
#                return imprimir_grid(p)
        elif vertical == False:
            if coluna > 5:
                print('ERROR 0035132.a51.x06')
            else:
                for i in range(5):
                    grid[linha][coluna+i] = 'P'
                return print(pd.DataFrame(p))
    else:
        print('Posição ocupada')


p = inicializarGrid()

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

print(pd.DataFrame(p))
posicionar_porta_avioes(p,2,8,True)



