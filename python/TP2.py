
palabra = ["peperina", "coleccion", "Marmota", "a"]
indice = 0

for x in palabra:
    primeraLetra = x[0]
    for caracter in x[1:]:
        if(primeraLetra == caracter):
            palabraNueva = x[1:].replace(caracter, "*") #palabra nueva es = eperina y le pido que reemplace el caracter repetido con un *
            palabra.pop(indice) #el metodo POP elimina un elemento de una lista con el indice que le pases
            palabra.insert(indice, (caracter + palabraNueva)) #el metodo INSERT inserta un elemento en la lista dependiendo el indice que le pases. En este caso yo le paso el indice 0 y le paso la palabra que quiero agregar que seria (CARACTER + PALABRANUEVA)
    indice = indice + 1 #una vez terminado el FOR sumo aumento el indice

print(palabra)