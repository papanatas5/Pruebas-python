
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


mi_lista = ("Santa", "Fe")
d1 =(mi_lista[0][:3])
d2 =(mi_lista[1][:1])
t1 =(mi_lista[0][3:])
t2 =(mi_lista[1][1:])
x = d1 + d2 + t1 + t2
print(x)


palabras = ("abcde", "xyz")
for x in palabras:
    if len(x) > 4:
        mitad1 = x[:3]
        mitad2 = x[3:]
        concatenacion = mitad2 + mitad1
        print(concatenacion)
    else:
        mitad3 = x[:2]
        mitad4 = x[2:]
        concatenacion = mitad4 + mitad3
        print(concatenacion)
print (mitad1 + mitad3 + mitad2 + mitad4)

palabras = ("abcd", "xy")
for x in palabras:
    if len(x) > 4:
        mitad1 = x[:3]
        mitad2 = x[3:]
        concatenacion = mitad2 + mitad1
        print(concatenacion)
    else:
        mitad3 = x[:1]
        mitad4 = x[1:]
        concatenacion = mitad4 + mitad3
        print(concatenacion)
print (mitad1 + mitad3 + mitad2 + mitad4)

#Enunciado 3
mi_lista = ["dos", "tres"]
for x in mi_lista:
    caracter1 = x [0] [:2]
    caracter2 = x [1] [:2]    
    y = x.replace(caracter1, caracter2)
    w = x.replace(caracter2, caracter1)
    print(y, w)
