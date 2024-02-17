import os 
import modulos.menu as menu
import main as m
import modulos.regproducts as r
def seeproducts(productsmain : dict):
    os.system('cls')
    print(menu.titulo)
    print('Estos son los productos registrados')
    for key in productsmain:
        print(key,productsmain)
    os.system('pause')