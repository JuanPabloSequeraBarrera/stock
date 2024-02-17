import os 
import main as m
import modulos.menu as menu
def cashpotential(productsmain : dict):
    os.system('cls') 
    print(menu.titulo)
    print('Bienvenido a la calculadora de ganancia de cada producto')
    print('Porfavor escriba el codigo del producto del cual quiere saber la ganacia potencial')
    codigo = int(input(':)_')) 
    if (codigo in productsmain):
        diferencia = (productsmain[codigo]['venta'] - productsmain[codigo]['compra'])
        multiplo = productsmain[codigo]['stock']
        gp = (diferencia * multiplo)
        nombre = productsmain[codigo]['nombre']
        print(f'La ganancia potencial de {nombre} es de {gp}')
# la gp se calcula mediante la diferencia de compra con la venta multiplicada por el stock