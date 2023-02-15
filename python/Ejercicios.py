### Ahorcado ###

# palabra = input("escribe una palabra: ")
# solucion = list("*" * len(palabra))
# fallos = 0
# while any(palabra) and fallos < 5:
#     letra = input("escribe una letra: ") 
#     if letra in palabra:
#         print ("Acierto")
#         i = palabra.index(letra)
#         palabra [i] = False
#         solucion [i] = letra
#     else:
#         print("Fallo")
#         fallos += 1
#     print(solucion)
# if fallos == 5:
#     print("Perdiste")
# else:
#     print("Ganaste")


## Ejercicio listas y tuplas ##
"""Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista."""

# my_list = ["matematicas", "fisica", "quimica", "historia", "lengua"]
# print (my_list)
# asignatura = my_list [:]
# print("yo estudio: ", asignatura )

# Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la nota que ha sacado en cada asignatura, y después las muestre por pantalla con el mensaje En <asignatura> has sacado <nota> donde <asignatura> es cada una des las asignaturas de la lista y <nota> cada una de las correspondientes notas introducidas por el usuario.

# my_other_list = ["matematicas", "fisica", "quimica", "historia", "lengua"]
# matematica_nota = input("que notas has sacado en matematicas?: ")
# fisica_nota = input("que notas has sacado en fisica?: ")
# quimica_nota = input("que notas has sacado en quimica?: ")
# historia_nota = input("que notas has sacado en historia?: ")
# lengua_nota = input("que notas has sacado en lengua?: ")

# print("en", (my_other_list [0]), "has sacado: ", matematica_nota)
# print("en", (my_other_list [1]), "has sacado: ", fisica_nota)
# print("en", (my_other_list [2]), "has sacado: ", quimica_nota)
# print("en", (my_other_list [3]), "has sacado: ", historia_nota)
# print("en", (my_other_list [4]), "has sacado: ", lengua_nota)

"""Maner mucho mas corta de hacerlo / no hecha por mi"""

# materias = ["matematicas", "fisica", "quimica", "historia", "lengua"]
# notas = []
# for materia in materias:
#     nota = input("¿Qué nota has sacado en " + materia + "?")
#     notas.append(nota)
# for i in range(len(materias)):
#     print("En", materias[i], "has sacado", notas[i])

#calculadora de iva

# def calculadora ():
#     total = input("total de la factura:")
#     iva=str( total + str((int(total) * 21)  / 100))
#     return str(iva)

# print(calculadora())

def invoice(amount, vat=21):
    """Función de aplica el IVA a una factura.
    Parametros
    amount: Es la cantidad sin IVA
    vat: Es el porcentaje de IVA
    Devuelve el total de la factura una vez aplicado el IVA. 
    """
    return amount + amount*vat/100

print(invoice(1000,10))
print(invoice(1000))