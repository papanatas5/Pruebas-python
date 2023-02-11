### Listas ###

my_list =  list ( )
my_other_list = [ ]

print( len(my_list) )

my_list =  [ 17, 24, 52, 30, 30, 35, 100]

print( my_list)
print( len(my_list) )

my_other_list = [ 17, 1.79, "Pedro", "Niello"]

print (type ( my_other_list ) )
print (type ( my_list ) )

print( my_other_list [ 0 ] )
print( my_other_list [ -1 ] )
print( my_other_list [ 3 ] )
print( my_other_list [ -4 ] )
# print( my_other_list [ 4 ] )  IndexError
# print( my_other_list [ -5 ] )  IndexError

print(my_list.count ( 30 ) ) #The count() method returns the number of times an item appears in a list

print( my_list. index ( 30 ) ) #The index() method returns the index of an item in the list

age, height,  name, surname = my_other_list 
print( name )

name, height, age, surname = my_other_list  [ 2 ], my_other_list[ 1 ], my_other_list [ 0 ], my_other_list [ 3 ]
print (name)

print( my_list + my_other_list )
# print( my_list * my_other_list ) Error

my_other_list.append ( "PedroTechnologies")
print( my_other_list )

my_other_list.insert ( 1, "Red")
print (my_other_list)

my_other_list [ 1 ] = "Black"
print (my_other_list)

my_other_list.remove ( "Black" )
print( my_other_list )

my_list.remove ( 30 )
print (my_list)

print(my_list.pop( ))
print(my_list)

my_pop = my_list.pop( 2 )
print(my_pop)
print(my_list)

del my_list [ 2 ]
print( my_list )

my_new_list = my_list.copy ( )

my_list.clear ( )
print (my_list )
print (my_new_list)  #imprime my_list en un punto anterior (en el punto en el que se copio)

my_new_list.reverse ( ) #The reverse() method reverses the order of a list.
print( my_new_list )

my_new_list.sort ( ) #The sort() method reorders the list items in ascending order and modifies the original list. If an argument of sort() method reverse is equal to true, it will arrange the list in descending order.
print( my_new_list )

print (my_new_list [ 1: 3 ])

my_new_list.extend ( my_other_list )
print (my_new_list )

my_list = "hola python"
print (my_list)
print ( type ( my_list ) )
