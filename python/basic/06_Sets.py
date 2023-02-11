### Sets ###

my_set = set ( )
my_other_set = { }
 
print(type(my_set))
print(type(my_other_set)) #inicialmente es un diccionario

my_other_set = {"Pedro", "Niello", 17}
print(type(my_other_set)) #Ahora es un set

print (len (my_other_set)) #Longitud

### Añadiendo un Elemento ###
my_other_set.add("PedroTech")

print(my_other_set) # Un set no es una estructura desordenada

my_other_set.add("PedroTech") # Un set no admite Repeticiones
print(my_other_set) 

# Chequear un dato esta #
print ("Pedro" in my_other_set)
print ("pedro" in my_other_set)

my_other_set.remove ("Niello")
print(my_other_set)

my_other_set.clear ()
print(len(my_other_set))

del my_other_set    
# print(my_other_set) name 'my_other_set' is not defined

my_set = {"Pedro", "Niello", 17}
my_list = list (my_set)
print(my_list)
print(my_list[0])

my_other_set = {"Naruto", "SNK", "kj"}

# Unions #

my_new_set = my_set.union(my_other_set)
print(my_new_set.union(my_new_set).union(my_set).union({"jujutsu kaisen", "Boruto"}))

#Difference#

print(my_new_set.difference(my_set)) #no aparece jk ni boruto, por que el union se hizo en el print y no en la variable

my_set_other_set = 17, 26, 32, 53

#Intersection#

print(my_new_set.intersection(my_set_other_set))

#Subset y Superset#

"""
Checking Subset and Super Set
A set can be a subset or super set of other sets:

Subset: issubset()
Super set: issuperset
# syntax
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.issubset(st1) # True
st1.issuperset(st2) # True
Example:

whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True

"""
### Remover y Pop ###
"""
Removing Items from a Set
We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.

# syntax
st = {'item1', 'item2', 'item3', 'item4'}
st.remove('item2')
The pop() methods remove a random item from a list and it returns the removed item.

Example:

fruits = {'banana', 'orange', 'mango', 'lemon'}
fruits.pop()  # removes a random item from the set
"""
#symetric difference#

st1 = {"item1", "item2", "item3"}
st2 = {"item2", "item3"}
print(st2.symmetric_difference(st1))

# joinin sets If two sets do not have a common item or items we call them disjoint sets. We can check if two sets are joint or disjoint using isdisjoint() method.#

print(st2.isdisjoint(st1)) #false tienen items en comun
st3 = {"item4", "item5"}

print(st2.isdisjoint(st3)) #true 
