# Python program to iterate over characters of a string

# Code #1
string_name = "geeksforgeeks"

# Iterate over the string
for element in string_name:
    print(element, end=' ')
print("\n")


# Code #2
string_name = "GEEKS"

# Iterate over index
for element in range(0, len(string_name)):
    print(string_name[element])

#min(), max()
#random.choice(list)
#random.choices(list, k=3)
l = [1, 2, 3, 4, 5]
evens = [i for i in l if i % 2 == 0]
print(evens)
