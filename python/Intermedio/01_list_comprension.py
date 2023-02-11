### lsit comprehension ###

my_original_list = [0, 1, 2, 3, 4, 5, 6, 7]
print(my_original_list)

my_range = range(8)
print(list(my_range))

my_list = list(i + 1 for i in range(8))
print(my_list)

my_list = list(i * 2 for i in range(8))
print(my_list)

my_list = list(i * i for i in range(8))
print(my_list)

def sum_five(number):
    return number + 5

my_list = list(sum_five(i) for i in range(8))
print(my_list)

#fuck
0, 1, 1, 2, 3, 5, 8, 13
def sum_fibonacci(resultnumber):
    return resultnumber + resultnumber 

fibonacci = list(sum_fibonacci (i) for i in range (15))