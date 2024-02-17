import os
import main as m 
import modulos.regproducts as r
import modulos.menu as menu
def changestock(productsmain : dict):
    os.system('cls')
    print(menu.titulo)
    print('Bienvenido al cambio de inventario del stock')
    print('seleccione el codigo del producto al que quiere modificar el stock')
    llave = int(input(':)_ '))
    if llave in productsmain:
        nuevovalor = int(input('Ingrese el nuevo valor de stock '))
        if (nuevovalor < productsmain[llave]['minimumstock']):
            print('El valor ingresado para el stock es menor al stock minimo permitido')
            changestock(productsmain)
        else:
            productsmain[llave]['stock'] = nuevovalor