### operadores aritmeticos ###

print ( 3 + 4 )
print  (3 - 4)
print (3 * 4)
print(3 / 4)
print(10 % 3)
print(10 // 3)
print(2 ** 3)

print( "Hola" + " " + " Python")
# print(int("hola") + int( "mundo"))
print( "hola " + str (5) )
print( "hola " * 2)

my_float = 2.5 * 2
print("hola "  *  int(my_float)) 


# Calculating area of a circle
radius = 10                                 # radius of a circle
area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
print('Area of a circle:', area_of_circle)

# Calculating area of a rectangle
length = 10
width = 20
area_of_rectangle = length * width
print('Area of rectangle:', area_of_rectangle)

# Calculating a weight of an object
mass = 75
gravity = 9.81
weight = mass * gravity
print(weight, 'N')                         # Adding unit to the weight

# Calculate the density of a liquid
mass = 75 # in Kg
volume = 0.075 # in cubic meter
density = mass / volume # 1000 Kg/m^3


    ### Operadores  Comparativos ###

print( 3 > 4 ) 
print ( 3 < 4 )
print ( 3 == 4)
print( 3 >= 4 )
print( 3 <= 4 )
print( 3 != 4 )

print( "hola" > "python")
print ( "hola" < "python")
print ( "hola" == "python")
print( "hola" <="python")
print( "hola" >= "python")
print( "hola" != "python")
print("hola" >= "zola")  #Ordenacion alfabetica por ASCII
print ("aaa" > "aba")  
print("AAA" < "aaa")
print(len("Hola") < len("python")) # Cuenta Caracteres

print('1 is 1', 1 is 1)                   # True - because the data values are the same
print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
print('coding' in 'coding for all') # True - because coding for all has the word coding
print('a in an:', 'a' in 'an')      # True
print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

   ### Operadores  Logicos ###

print( 3 > 4 and "hola" > "python")
print( 3 > 4 or "hola" > "python")
print( 3 < 4 and "hola" < "python")
print( 3 < 4 or "hola" < "python")
print( 3 < 4 or "hola" < "python" and 4 == 4)
print( not ( 3 > 4 ) )

print(3 > 2 and 4 > 3) # True - because both statements are true
print(3 > 2 and 4 < 3) # False - because the second statement is false
print(3 < 2 and 4 < 3) # False - because both statements are false
print('True and True: ', True and True)
print(3 > 2 or 4 > 3)  # True - because both statements are true
print(3 > 2 or 4 < 3)  # True - because one of the statements is true
print(3 < 2 or 4 < 3)  # False - because both statements are false
print('True or False:', True or False)
print(not 3 > 2)     # False - because 3 > 2 is true, then not True gives False
print(not True)      # False - Negation, the not operator turns true to false
print(not False)     # True
print(not not True)  # True
print(not not False) # False

mi_segundos_por_dia = 60 * 60 * 24
mes = 30
age = 17
print( "mi segundo de vida son",  (mi_segundos_por_dia * mes * age) ) #no olvidarse de las comas
