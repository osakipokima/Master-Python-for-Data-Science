#
# Example file for working with functions
#

# define a basic function
def func1():
    print("I am a function. I pull up to the function")

# function that takes arguments
def func2(arg1, arg2):
    print(arg1, " ", arg2)


# function that returns a value
def cube(x):
    return x*x*x

# function with default value for an argument
def power(num, x=1):
    result = 1
    for i in range(x):
        result = result * num
    return result

#function with variable number of arguments
def multi_add(*args):
    result = 0
    for x in args:
        result = result + x
    return result

# func1()  #function is called directly executes call of the function
# print(func1()) #function is called within the print function

# #since we didn't call the function in print, it prints none and the value of the function itself
# #the output is an example of how functions are objects
# print (func1) 
# func2 (10,20)
# print (func2(10,20))
# print (cube(3))
print(power(2))
print(power(2,3))
print(power(x=3, num=2))
print(multi_add(4,5,6,12,8))

