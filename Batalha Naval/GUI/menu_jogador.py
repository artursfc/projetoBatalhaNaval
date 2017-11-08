from logica import main
from GUI import menu_principal


def mostrar_menu():
    run_menu = True
   

    menu = ("\n+------------------+\n"+
             "(1) Atirar --------- \n" +
             "(0) Voltar ---------\n"+
            "+------------------+\n")
    
    while(run_menu):
        print (menu)
        
        op = int(input("Digite sua escolha: \n"))

        if (op == 1):
            main.atirar()
        elif (op == 0):
            menu_principal.mostrar_menu
            run_menu = False
        else:
            print ("Valor invalido")
if __name__ == "__main__":
    mostrar_menu()
