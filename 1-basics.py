# import modules
import sys
from matplotlib import pyplot as plt

"""
note to reader: I've included a bunch of sys.exit() for demonstration purposes. 
delete them if they're giving you trouble
"""

# data types
num_int: int = 5
num_float: float = 5.5
val_bool: bool = True

#print(type(num_int), num_int)


# arrays
list_ary: list = [0, 1, 1, 2, 3, 5, 8, 13] # mutable
tuple_ary: tuple = (0, 1, 1, 2, 3, 5, 8, 13) # immutable
string_ary: str = "This is a string"

#print("First index = ", string_ary[1])

#sys.exit()

# array quirks
list_ary[2] = 10
#tuple_ary[2] = 10

an_ary = list_ary
an_ary[2] = 10
#print(list_ary)
#sys.exit()

another_ary = list_ary.copy()
another_ary[3] = 45
#print(list_ary[3])
#sys.exit()

# dict
basic_dict = dict(key1=1, key2=4, key3=34)
#print(basic_dict["key1"])
#sys.exit()

# logic statements
"""number = int(input("input number greater than 50: "))
if number > 50:
    print("yes!")
elif number > 40:
    print("close!")
else:
    print("no!")
sys.exit()"""

# for vs while loop
"""for i in range(0, 10):
    print(i)

sys.exit()"""

#print() # empty line
"""i = 10
while i > 1:
    print(i)
    i -= 1
sys.exit()"""

# real use?
num_entries = 20
sequence = (0,1)
i = 2
while i < num_entries:
    sequence.append(sequence[i-1] + sequence[i-2])
    i += 1

print(sequence)

# could we do this with a while loop? with a tuple?