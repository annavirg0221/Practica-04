opcion1=("1)Agregar un articulo a la lista")
opcion2=("2)Eliminar un articulo de la lista")
opcion3=("3)Mostrar la lista completa")
opcion4=("4)Salir")

Menú=dict([("opcion1", opcion1), ("opcion2", opcion2), ("opcion3", opcion3), ("opcion4", opcion4)])
for opcion in Menú:
    print(Menú[opcion])

lista_de_compras=[]
while True:
    
    numero_menu=input("ingrese una opcion del Menú: ")
    if numero_menu=='4':
        print("Termino su compra")
        break
    if numero_menu=='1':
        articulo=input("ingrese el nombre del articulo para su lista de compras: ")
        lista_de_compras.append(articulo)
        print("Su lista de compras es: ", lista_de_compras)
        print("\n")
        Menú=dict([("opcion1", opcion1), ("opcion2", opcion2), ("opcion3", opcion3), ("opcion4", opcion4)])
        for opcion in Menú:
            print(Menú[opcion])
    if numero_menu=='2':
        eliminar=input("ingrese el nombre del articulo que desea eliminar: ")
        lista_de_compras.remove(eliminar)
        print("Su nueva lista de comrpas es: ", lista_de_compras)
        print("\n")
        Menú=dict([("opcion1", opcion1), ("opcion2", opcion2), ("opcion3", opcion3), ("opcion4", opcion4)])
        for opcion in Menú:
            print(Menú[opcion])

    if numero_menu=='3':
        for articulo in lista_de_compras:
            print(articulo)
            print("\n")
            Menú=dict([("opcion1", opcion1), ("opcion2", opcion2), ("opcion3", opcion3), ("opcion4", opcion4)])
            for opcion in Menú:
                print(Menú[opcion])
             
    else:
        print('Error, no ingreso un elemento de la lista, intente de nuevo') 
         
