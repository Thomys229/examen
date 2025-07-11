productos = {'8475HD': ['HP', 15.6, '8GB', 'DD', '1T', 'Intel Core i7', 'Nvidia GTX1050'],
'2175HD': ['Acer', 14, '4GB', 'SSD', '512GB', 'Intel Core i7', 'Nvidia GTX1050'],
'JjfFHD': ['Asus', 14, '16GB', 'SSD', '256GB', 'Intel Core i5', 'Nvidia RTX2080Ti'],
'fgdxFHD': ['HP', 15.6, '12GB', 'DD', '1T', 'Intel Core i5', 'integrada'],
'GF75HD': ['Asus', 15.6, '12GB', 'DD', '1T', 'Intel Core i3', 'Nvidia GTX1050'],
'123FHD': ['Acer', 14, '6GB', 'DD', '1T', 'AMD Ryzen 7', 'integrada'],
'342FHD': ['Acer', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
'UWU131HD': ['Dell', 15.6, '8GB', 'DD', '1T', 'AMD Ryzen 5', 'Nvidia GTX1050'],
}

stock = {'8475HD': [387990,10], '2175HD': [327990,4], 'JjfFHD': [424990,1],
'fgdxFHD': [664990,21], '123FHD': [290890,32], '342FHD': [444990,7],
'GF75HD': [749990,2], 'UWU131HD': [349990,1], 'FS1230HD': [249990,0],
}

#stock por marca
def stock_marca(marca):
    total = 0
    for codigo, datos in productos.items():
        if(datos[0].lower() == marca.lower()):
            total += stock[codigo][1]
    print(f"El stock de la marca:{marca} es:{total}")

#busqueda por precio 
p_min = 0 
p_max = 0
def buscar_precio(p_min, p_max):
    resultados = []
    for codigo, datos in stock.items():
        precio = datos[0]
        if(precio >= p_min and precio <= p_max) and (stock[codigo][0] > 0 ):
            resultados.append(codigo + "-" + str(datos[1]))
    if resultados:
        resultados
        print(f"Productos:, {resultados}")
    else:
        print("No hay notebook disponibles para mostrar.")

#lista de productos 
def ordenar_productos():
   print("----------Productos Ordenados----------")
   print(productos)
   print("---------------------------------------")


#Menu
def main():
    while True:
        print("___MENU___")
        print("1)Stock marca\n2)Busqueda por precios\n3)Listado de productos\n4)Salir")
        
        opc=int(input("Ingese una opcion: "))

        if(opc == 1):
            marca=input("Ingrese la marca: ")
            stock_marca(marca)
        elif(opc == 2 ):
            p_min = int(input("Ingrese el precio minimo: "))
            p_max = int(input("Ingrese el precio maximo: "))
            buscar_precio(p_min,p_max)
        elif(opc == 3 ):
            ordenar_productos()
        elif(opc == 4):
            print("Programa finalizado.")
            break
        else:
            print("La opcion no es valida")
if(__name__ == "__main__"):
    main()  