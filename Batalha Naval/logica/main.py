from GUI import menu_jogador
import random

import principal

def initPgrid():
    global pgrid
    pgrid = inicializarGrid()

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
                        return grid
                 else:
                        initGame()
            elif vertical == False:
                if coluna > 5:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(5):
                            grid[linha][coluna+i] = 'P'
                        return grid
                    else:
                        initGame()
        else:
            initGame()


def posicionar_encouracado(grid,linha,coluna,vertical):
        size = 4
        if grid[linha][coluna] == '.':
            if vertical == True:
                 if linha > 6:
                    print('Inválido. Fora da grid')
                 elif check_pos_ver(grid,linha,coluna,size) == True:
                        for i in range(4):
                            grid[linha+i][coluna] = 'E'
                        return grid
                 else:
                        initGame()
            elif vertical == False:
                if coluna > 6:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(4):
                            grid[linha][coluna+i] = 'E'
                        return grid
                    else:
                        initGame()
        else:
            initGame()
            
def posicionar_cruzador(grid,linha,coluna,vertical):
        size = 3
        if grid[linha][coluna] == '.':
            if vertical == True:
                 if linha > 7:
                    print('Inválido. Fora da grid')
                 elif check_pos_ver(grid,linha,coluna,size) == True:
                        for i in range(3):
                            grid[linha+i][coluna] = 'C'
                        return grid
                 else:
                        initGame()
            elif vertical == False:
                if coluna > 7:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(3):
                            grid[linha][coluna+i] = 'C'
                        return grid
                    else:
                        initGame()
        else:
            initGame()

def posicionar_sub(grid,linha,coluna,vertical):
        size = 2
        if grid[linha][coluna] == '.':
            if vertical == True:
                 if linha > 8:
                    print('Inválido. Fora da grid')
                 elif check_pos_ver(grid,linha,coluna,size) == True:
                        for i in range(2):
                            grid[linha+i][coluna] = 'S'
                        return grid
                 else:
                        initGame()
            elif vertical == False:
                if coluna > 8:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(2):
                            grid[linha][coluna+i] = 'S'
                        return grid
                    else:
                        initGame()
        else:
            initGame()


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

def imprimir_grid():
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
     
def imprimir_pgrid():
     cabeçalho = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
     print(0 ,'', cabeçalho)
     cont = 1
     for i in pgrid:
         if cont == 10:
             print(cont,end=' ')
             print(i)
             break
         print(cont, end = "  ")
         print(i)
         cont += 1
     print('\n')
     
#def checkPast(linha,coluna,tiros):
#    for i in range(len(tiros)):
#        print(i)
#        for j in range(len(tiros[i])):
#            print(j)
#            if linha == tiros[i][j] and coluna == tiros[i][j]:
#                return True
#            else:
#                return False

def atirar():
    c = 0 #contador para o numero de vezes que o jogador vai atirar
    aux_l = 100
    aux_c = 100
#    tiros = []
    cont_p = 0
    cont_e = 0
    cont_c = 0
    cont_s = 0
    end = 0
    while c < 20:
        linha = int(input("Insira a linha: "))        
        while linha < 0 or linha > 9:
            linha = int(input("Valor inválido. Insira a linha:"))
        coluna = int(input("Insira a coluna: "))
        while coluna < 0 or coluna > 9:
            coluna = int(input("Valor inválido. Insira a coluna:"))
        
        while linha == aux_l and coluna == aux_c:
           print('\nCuidado, você escolheu o mesmo local da ultima jogada')
           linha = int(input('Insira a linha: '))
           coluna = int(input('Insira a coluna: '))

#        while checkPast(linha,coluna,tiros) == True:
#            print("\nCuidado, você já escolheu este local antes\n")
#            linha = int(input("Insira a linha: "))        
#            while linha < 0 or linha > 9:
#                linha = int(input("Valor inválido. Insira a linha:"))
#            coluna = int(input("Insira a coluna: "))
#            while coluna < 0 or coluna > 9:
#                coluna = int(input("Valor inválido. Insira a coluna:"))

        if grid[linha][coluna] == ".":
            print ("\nTiro na água!!!\n")
            grid[linha][coluna] = "."
            c += 1
        elif grid[linha][coluna] == "P":
            print("\nPorta-Aviões atingido!!!\n")
            grid[linha][coluna] = "p"
            pgrid[linha][coluna] = "X"
            c += 1
            cont_p += 1
            
        elif grid[linha][coluna] == "E":
            print ("\nEncouraçado atingido!!!\n")
            grid[linha][coluna] = "e"
            pgrid[linha][coluna] = "X"
            c += 1
            cont_e += 1
        elif grid[linha][coluna] == "S":
            print ("\nSubmarino atingido!!!\n")
            grid[linha][coluna] = "s"
            pgrid[linha][coluna] = "X"
            c += 1
            cont_s += 1
        elif grid[linha][coluna] == "C":
            print ("\nCruzador atingido!!!\n")
            grid[linha][coluna] = "c"
            pgrid[linha][coluna] = "X"
            c += 1
            cont_c += 1
        aux_l = linha
        aux_c = coluna
#        tiros.append([linha,coluna])
        if cont_p >= 5:
            print("\nPorta-aviões destruído!!\n")
            end += 1
            cont_p = 0
            if end >= 4:
                print("\nVITÓRIA\n")
                break
        if cont_e >= 4:
            print("\nEncouraçado destruído!!\n")
            end += 1
            cont_e = 0
            if end >= 4:
                print("\nVITÓRIA\n")
                break
        if cont_c >= 3:
            print("\nCruzador destruído!!\n")
            end += 1
            cont_c = 0
            if end >= 4:
                print("\nVITÓRIA\n")
                break
        if cont_s >= 2:
            print("\nSubmarino destruído!!\n")
            end += 1
            cont_s = 0
            if end >= 4:
                print("\nVITÓRIA\n")
                break
        imprimir_pgrid()
    print("\nDERROTA\n")
    principal.principal()


def initGame():
    global grid
    grid = inicializarGrid()
    initPgrid()
    while "P" not in grid:
        posicionar_porta_avioes(grid,random.randint(1,5),random.randint(1,5),bool(random.getrandbits(1)))
        break
    while "E" not in grid:
        posicionar_encouracado(grid,random.randint(1,6),random.randint(1,6),bool(random.getrandbits(1)))
        break
    while "C" not in grid:
        posicionar_cruzador(grid,random.randint(1,7),random.randint(1,7),bool(random.getrandbits(1)))
        break
    while "S" not in grid:
        posicionar_sub(grid,random.randint(1,8),random.randint(1,8),bool(random.getrandbits(1)))
        break
    menu_jogador.mostrar_menu()
    print("\n" * 100)
    return grid
