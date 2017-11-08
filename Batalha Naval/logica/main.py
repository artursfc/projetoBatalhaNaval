from GUI import menu_jogador
import random

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
                        print('Posição ocupada')
            elif vertical == False:
                if coluna > 5:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(5):
                            grid[linha][coluna+i] = 'P'
                        return grid
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
                        return grid
                 else:
                        print('Posição ocupada')
            elif vertical == False:
                if coluna > 6:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(4):
                            grid[linha][coluna+i] = 'E'
                        return grid
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
                        return grid
                 else:
                        print('Posição ocupada')
            elif vertical == False:
                if coluna > 7:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(3):
                            grid[linha][coluna+i] = 'C'
                        return grid
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
                        return grid
                 else:
                        print('Posição ocupada')
            elif vertical == False:
                if coluna > 8:
                    print('Inválido. Fora da grid')
                else:
                    if check_pos_hor(grid,linha,coluna,size) == True:
                        for i in range(2):
                            grid[linha][coluna+i] = 'S'
                        return grid
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

def atirar():
    c = 0 #contador para o numero de vezes que o jogador vai atirar
    aux_l = 100
    aux_c = 100
    while c < 20: 
        linha = int(input("Insira a linha: "))
        coluna = int(input("Insira a coluna: "))
        while linha == aux_l and coluna == aux_c:
            print('\nCuidado, você escolheu o mesmo local da ultima jogada')
            linha = int(input('Insira a linha: '))
            coluna = int(input('Insira a coluna: '))

        if grid[linha][coluna] == ".":
            print ("\nTiro na água!!!\n")
            grid[linha][coluna] = "*"
            c += 1
        elif grid[linha][coluna] == "P":
            print("\nPorta-Aviões atingido!!!\n")
            grid[linha][coluna] = "p"
            c += 1
        elif grid[linha][coluna] == "E":
            print ("\nEncouraçado atingido!!!\n")
            grid[linha][coluna] = "e"
            c += 1
        elif grid[linha][coluna] == "S":
            print ("\nSubmarino atingido!!!\n")
            grid[linha][coluna] = "s"
            c += 1
        aux_l = linha
        aux_c = coluna


def initGame():
    global grid
    grid = inicializarGrid()
    print(grid)
    while "P" not in grid:
        posicionar_porta_avioes(grid,random.randint(0,2),random.randint(0,2),bool(random.getrandbits(1)))
        break
    while "E" not in grid:
        posicionar_encouracado(grid,random.andint(3,4),random.randint(3,4),bool(random.getrandbits(1)))
        break
    while "C" not in grid:
        posicionar_cruzador(grid,random.randint(5,7),random.randint(5,7),bool(random.getrandbits(1)))
        break
    while "S" not in grid:
        posicionar_sub(grid,random.randint(7,9),random.randint(7,9),bool(random.getrandbits(1)))
        break
    print(grid)

    menu_jogador.mostrar_menu()
    print("\n" * 100)
    return grid

if __name__ == "__main__":
    mostrar_menu()
