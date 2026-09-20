import sys

# function definition
def basic_adder(input1, input2):
    return input1 + input2

# function implementation
#print(basic_adder(3.1,5.12))
#sys.exit()

# type hinting
def assign(name:str, num1:int|float=1, num2:int|float=0.1) -> list:
    return [name, num1, num2]

"""print(assign(name="list1", num2=-5.13, num1=3.1))
sys.exit()"""

# args & kwargs
def advanced_adder(*args:int|float) -> float:
    # args is a tuple
    sum = 0.0
    for val in args:
        sum += val

    return sum

#print(advanced_adder(1, 2, 3, 4, 5))
#sys.exit()

def set_options(**kwargs) -> dict:
    options = dict()
    for pair in kwargs.items():
        options[pair[0]] = pair[1]
    return options

print(set_options(option1="yes", option2="no", option3="yes"))