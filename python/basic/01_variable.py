# variables
mi_variable = "my string variable"
print (mi_variable)

mi_complex_variable = "1 + 2j"
print (mi_complex_variable)

mi_int_variable = 3
print(mi_int_variable)

mi_int_to_str_variable = str(mi_int_variable)
print(mi_int_variable)
print(type(mi_int_to_str_variable))

#concadenacion de variables
print (mi_variable, mi_complex_variable)
print("este es el valor de:",mi_complex_variable)

# str = cadena de texto 
# algunas funciones del sistema
print (len (mi_complex_variable))

# variables en una sola linea, peligroso puede ser un foco de errores
name, surname, age = "mi nombre es pedro", "niello", 17 #el 17 nes un int y lo demas es str
print( name, surname," y tengo ", age)

# input, el programa "pregunta", el usuario responde y escribe las respuestas
"""
name = input('What is your name: ')
age = input('How old are you? ')

print(name)
print(age)
"""
# Al haber variables del mismo nombre queda la ultima variable como definitiva, es hecho en cascada

#cambiamos su tipo
name = 45
age = "pedro"

print (name, age)

# ¿forzamos el tipo? - no
adress: str = "25 de mayo"
adress = 17
print(adress)

