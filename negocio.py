import menu
import utiles

dec = 0



while dec!=5:
    if dec == 1:
        utiles.ingresoproducto()
    elif dec == 2:
        utiles.venta()
    
    elif dec == 4:
        utiles.mostrar()

    elif dec == 6:
        utiles.newprecio()

    dec = menu.imprimir()
        
print("aca termino el codigo")


