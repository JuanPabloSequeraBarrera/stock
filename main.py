import os 
import modulos.menu as m
import modulos.regproducts as r
import modulos.visualize as v
import modulos.changestock as c
import modulos.ganancia as g
if __name__ == '__main__':
    productsmain = {}
    isActive = True
    while isActive:
        os.system('cls')
        op = m.menu()
        if (op == 1):
            r.regist(productsmain)
        elif(op == 2):
            v.seeproducts(productsmain)
        elif(op == 3):
            c.changestock(productsmain)
        elif(op == 4):
            pass
        elif(op == 5):
            g.cashpotential(productsmain)
        elif(op == 6):
            isActive = False
            print('Muchas gracias por usar el software')

