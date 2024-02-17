import os
lstopciones = [1,2,3,4,5,6]
isActive = True
titulo = """
    +++++++++++++++++++++++++++++
    + GESTOR DE INVENTARIO S.A.S+
    +++++++++++++++++++++++++++++
"""
opciones = ('1.Registro de productos\n2.Visualizacion de productos\n3.Actualizacion de Stock\n4.Informe de productos criticos\n5.Ganancia potencial de stock\n6.Salir')
def menu():
    os.system('cls')
    print(titulo)
    print(opciones)
    try:
        options = int(input(':)_ '))
        if not (options in lstopciones):
            print('Numero no valido')
    except ValueError:
        print('Error de digitacion')
        os.system('pause')
        menu()
    else:
        return options
    

    
