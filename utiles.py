import menu
# hacer una lista que sirva para un negocio donde tenga:
# listacodigo
# lista de la descripcion
# lista de precio 



"""
ABM ----> LISTAS ASOCIADAS A LOS PRODUCTOS
A (alta)
M (modificacion)

"""



""""


menu = 
ingresar producto:CODIGO DE PRODUCTO,CANTIDAD VENDIDA, PRECIO TOTAL
actualizar precio
generar una venta
nombre del cliente


"""

listacodigoventa = []
listacliente = []
listapreciototal = []
listacantventa = []

listacodigo = []
listaprecio = []
listadecr = []
listacant = []

def newprecio ():
    code = int(input("ingrese el codigo del producto"))
    precio = int(input("ingrese el nuevo precio"))
    pos = buscarpos(code)

    listaprecio[pos] = precio

        
    


def buscarpos (codigo):
    for i in range (0,len(listacodigo)):
        if codigo == listacodigo[i]:
            pos = i

            return pos


def venta ():
    
    nombre = (input("ingrese su nombre"))
    cantidad = int(input("ingrese la cantidad que quiere vender"))
    precio = codbusq(listacodigo, listaprecio)
    total = cantidad*precio

    return total


def ingresoproducto():
    
    codigo = int(input("ingrese el codigo del producto "))
    precio = int(input("ingrese el precio del producto "))
    cant = int(input("ingrese la cantidad "))
    decr = (input("ingrese una descripcion del producto "))

    listacodigo.append(codigo)
    listaprecio.append(precio)
    listacant.append(cant)
    listadecr.append(decr)
    
    


  
def codbusq (listacodigo,listaprecio):

    code = int(input("ingrese el codigo"))
    for i in range(0,len(listacodigo)):
        
        if listacodigo [i] == code:
            pos = i
    for i in range (0,len(listaprecio)):
        if i== pos:
            precio = listaprecio[i]
            
            return precio
    
    
    return precio 
            

def mostrar ():
    print(listadecr)
