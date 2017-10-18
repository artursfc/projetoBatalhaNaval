# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 16:44:43 2017

@author: Artur
"""

from logica import main

def mostrar_menu():
    run_menu = True
   

    menu = ("\n+------------------+\n"+
             "(1) Iniciar jogo --- \n" +
             "(2) Como jogar ----- \n" +
             "(0) Sair -----------\n"+
            "+------------------+\n")
    
    while(run_menu):
        print (menu)
        
        op = int(input("Digite sua escolha: "))

        if (op == 1):
            main.inicializarGrid()
        elif(op == 2):
            como_jogar = ('\n+-------------------------------------------------------------------+ \n'+
                          '> Após iniciar o jogo, será disponibilizado 20 tiros para o jogador - \n'+
                          '--> Para atirar é necessário informar a linha e a coluna ------------ \n'+
                          '--> Após cada tiro será informado se foi um acerto ou não ----------- \n'+
                          '+-------------------------------------------------------------------+ \n')
            print(como_jogar)
        elif (op == 0):
            print ("\n>>>>> Saindo do jogo <<<<<")
            run_menu = False
        else:
            print ("Valor invalido")
