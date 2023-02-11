 ### strings ###

mi_string = "mi string"
mi_other_string = "mi otro string"

print ( len(mi_string))
print ( len(mi_other_string))

mi_nueva_linea_string = "este es un string  \n con salto de linea"
print( mi_nueva_linea_string)

mi_tab_string = "\t este es un string con tabulacion"
print ( mi_tab_string)

mi_scape_string = "\t este es un string \n escapado"
print( mi_scape_string )

# Formateo

name, surname, age = "pedro", "niello", 17

print ( "mi nombre es {} {} y mi edad es {}" .format (name, surname, age))
print ( "mi nombre es %s %s y mi edad es %d" %(name, surname, age))
print ( f"mi nombre es {name} {surname} y mi edad es {age}")

# Desempaquetado de caracteres

language = "python"
a, b, c, d, e, f = language
print (a)
print (e)

# Division

language_slice = language [ 1 : 3 ]
print (language_slice)

language_slice = language [ 1 :  ]
print (language_slice)

language_slice = language [ -2 ]
print (language_slice)

language_slice = language [ 1 : 2 : 4 ]
print (language_slice)

language_slice = language [ 0 : 6 : 2 ]
print (language_slice)

# reverse
reversed_language = language [ :: -1 ]
print (reversed_language)

# Funciones

print( language.capitalize())  #lo pone en mayuscula
print( language.upper())    #Mayusculas
print(language.count("t"))  #cuenta las t
print(language.isnumeric())    #es un numero?
print ( language.lower() )  #minusculas
print ( "1" .isnumeric ( ) ) 
print ( language.upper( ). isupper( ) ) 
print ( language.startswith ( "py" ) )
print ( language.startswith ( "Py" ) )
print (not language.startswith ( "py" ) )
print( "Py" == "py" )
