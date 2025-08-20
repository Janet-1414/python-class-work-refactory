# a for loop - repeats some code a certain number of times
for i in range(3):
    print("Hello", i)

# an if condition - runs code only if a condition is True
x = 5
if x > 3:
    print("x is greater than 3")

# an if else condition - runs one block if True, another if False
y = 2
if y > 3:
    print("y is greater than 3")
else:
    print("y is not greater than 3")

# a function - a reusable block of code that does something
def greet():
    print("Hi there!")

# a function definition - creating/writing a function (above is an example)
# a function invocation - calling/executing the function
greet()

# a parameter - a variable used inside a function to accept input
def greet_person(name):  # 'name' is a parameter
    print("Hello", name)

# a parameter list - all parameters inside parentheses in function definition
def add_numbers(a, b):  # 'a' and 'b' form the parameter list
    return a + b

# an argument - the actual value you give to a function when calling it
greet_person("Janet")  # "Janet" is an argument

# passing an argument - giving a value to the function's parameter (example above)

# a return statement - sends a value back from the function
result = add_numbers(2, 3)  # 2 and 3 are arguments, result will be 5
print(result)

# a module - a Python file with code you can reuse
# e.g., math is a built-in module
import math
print(math.sqrt(16))

# a package - a collection of modules in folders
# e.g., 'numpy' is a package that has many modules for math operations

# an import statement - used to bring in modules or packages
# already shown above: import math
