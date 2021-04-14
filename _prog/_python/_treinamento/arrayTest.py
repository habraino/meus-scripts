from array import *

my_array = array('i', [1, 2, 3, 4])
my_array.append(5) # appending new value in my_array
my_array.insert(0, 0) # inserting the value

for index, item in enumerate(my_array):
    print('Position: {} :: Item: {}'.format(index, item))

# extend new array in my array
my_extend_array = array('i', [6, 7, 8, 9])
my_array.extend(my_extend_array)

print('*'*20)
for i in range(0, len(my_array)):
    print(i)

# Add items from list into array using fromlist() method
my_array2 = array('i', [1, 2, 3, 4])
c = [5, 6, 7, 8]

my_array2.fromlist(c)

print("Added list: ", my_array2)

# Remove any array element using remove() method
my_array2.remove(5)
print("Remove any: ", my_array2)

# Remove last array element using pop() method
my_array2.pop()
print("Remove last: ", my_array2)

# Fetch any element through its index using index() method
print("Index 4: ", my_array2.index(4))

# Reverse a python array using reverse() method
print("Array reversed: ", my_array.reverse())


