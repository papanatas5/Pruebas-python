### tuples ###
"""Conjunto de valores inmutables """

my_tuple = tuple ( )
my_other_tuple = ( )

my_tuple = ( 17, 1.79, "Pedro", "Niello", "Pedro" )
print (my_tuple)
print (type (my_tuple))

print(my_tuple[0])
print(my_tuple[-1])
# print(my_tuple[-4])  IndexError
# print(my_tuple[-6])  IndexError

#Index y Count#

print (my_tuple.count ("Pedro"))
print (my_tuple.index ("Niello"))
print (my_tuple.index ("Pedro"))

# my_tuple [ 1 ] = 1.86 'tuple' object does not support item assignment

# Suma de Tuplas #

my_sum_tuple = my_tuple + my_other_tuple 
print ( my_sum_tuple )

print (my_sum_tuple [3:6])

# Cambiando a una lista para agregar datos #

my_tuple = list(my_tuple)
print(type(my_tuple))

my_tuple [4] = "PedroTechnologies"
my_tuple.insert (1, "verde")
my_tuple = tuple (my_tuple)
print(my_tuple)
print(type(my_tuple))

# items #

print ("Pedro" in my_tuple) #true / chequea si un item esta en la tupla y devuelve un booleano

# eliminacion #

# del my_tuple [ 2 ] 'tuple' object doesn't support item deletion
# del my_tuple name 'my_tuple' is not defined / no es un clear como en las listas

print (my_tuple) 
