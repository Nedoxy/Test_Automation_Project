"""
Parameters are variables defined within the parentheses of your function that allows you to receive values in your fxn.

Arguments are the values sent to your fxn.
parameters are optional in python.

5 types of argument:
1. Required
2. Default
3. Keyword
4. Arbitrary
5. Arbitrary keyword arg


1. The required argument are those that must be passed when calling a fxn in the order that the parameter are declared.
"""


def add(num1, num2):
    print(num1 + num2)


add(2, 3)

"""The parameters must num1 & num2 are required and are passed in the order when invoking the add fxn"""


""" 
2. Default arg uses the parameter default value if the fxn is invoked without passing the argument value.

3. Keyword parameter is used to identify which parameter the value is for by the parameter name. When using the keyword 
argument, the order doesn't matter.

"""


number = 10


def convert(number):
    feet = number * 3.281
    return feet


print(number, "\b" "m" " =", convert(number), "\b" 'ft')

print("\nRequired parameter/ argument")


def greet(name):
    print("Hello", name)


greet("Jide")

print("\nDefault argument")


def add(num1, num2=3):
    print(num1 + num2)


add(2, 6)

print(
    "\nKeyword Arguments")  # the order the values are entered does not matter,as long as the position has been
# previously defined


def minus(num1, num2):
    result = num1 - num2
    print("answer =", result)


minus(num1=5, num2=3)
minus(num2=3, num1=10)

print("\nArbitrary Arguments")


def add(*args):
    print(args[0] + args[0] + args[2])


add(2, 3, 4)


def print_value(*args):
    print("Args:", args, args[1])


# print_value()
# print_value(1)
print_value(1, 2)
print_value(1, 2, 3)

print("\nArbitrary Keyword Arguments")


def print_kvalue(**kargs):
    print("kArgs:", kargs, kargs['num1'], kargs['num2'])


print_kvalue(num1=1, num2=3)

print("\nReturn Statement")


def add_and_return(num1, num2):
    result = num1 + num2
    return result


res = add_and_return(50, 50)
print("50 + 50:", res)

print("using return to prematurely terminate a codeblock")


def check_number(number):
    if number > 5:
        return
    print("Number:", number)


check_number(1)
check_number(3)
check_number(5)
check_number(6)
check_number(10)
