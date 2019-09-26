# # 
# # Example file for variables
# #

# # Declare a variable and initialize it
f=0
# print(f)


# # # re-declaring the variable works
# f="abc"
# print(f)

# # # ERROR: variables of different types cannot be combined
# print("this is a string " + str(123))

# Global vs. local variables in functions
def someFunction():
    # "def" gets printed since we called global and so will print(f) at the end
    global f
    f = "def"
    print(f)
# def will be printed first from the local variable inside the function
someFunction()
# 0 will be printed since f is a global variable defiend
print(f)

del f
print(f)


