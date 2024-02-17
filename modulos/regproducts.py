import os
import modulos.menu as menu
import main as m
def regist(productsmain : dict):
    os.system('cls')
    print(menu.titulo)
    print('Bienvendio al registro de productos de la tienda')
    try:
        print('Porfavor escriba el nombre del producto a agregar')
        name = str ((input(':)_ ')).upper())
        print(f'Porfavor ingrese el codigo de {name} (solo numeros enteros)')
        code = int ((input(':)_ ')))
        if (code in productsmain):
            print('codigo ya en uso, porfavor escoja otro')
            os.system('pause')
            regist(productsmain)
        print(f'Porfavor escriba el valor de compra de {name} en dolares')
        buy = float ((input(':)_ ')))
        print(f'Porfavor escriba el valor de venta de {name} en dolares')
        sell = float ((input(':)_ ')))
        print(f'Porfavor escriba el numero de stock de {name}')
        stock = int ((input(':)_ ')))
        print(f'Porfavor escriba el minimo de stock de {name}')
        minstock =int ((input(':)_ ')))
        if (stock < minstock):
            print('La cantidad de stock no puede ser menos que el minimo de stock')
            os.system('pause')
            regist(productsmain)
        print(f'Porfavor escriba el maximo de stock de {name}')
        maxstock = float ((input(':)_ ')))
        print(f'Porfavor escriba el nombre del proovedor de {name}')
        proveedor = str((input(':)_ ')).upper())
        producto = {
            'codigo': code,
            'nombre': name,
            'compra': buy,
            'venta' : sell,
            'stock' : stock,
            'minimumstock' : minstock,
            'maximumstock' : maxstock,
            'proveedor' : proveedor
        }
        productsmain.update({code:producto})
        print(f'El producto {name} ha sido registrado correctamente, desea agregar otro? Si(si) No(no)')
        decis = str ((input(':)_ ')).upper())
        if (decis == 'NO' ):
            os.system('pause')
        else:
            regist(productsmain)
    except ValueError:
        print('dato invalido')
        regist(productsmain)