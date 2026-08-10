"""
variable scope and functions

write a function that takes any number and returns it multiplied by two
"""
x = 4

text = ['this', 'is', 'a', 'sentence']

def math(num1, num2):
    y = 4
    text = 'string'
    def multiply(num): 
        global x 
        nonlocal y 
        x = 5
        y = 5
        print('this is a function')
        print(f'x is {x}, y is {y}')
        return num
    
    multiply(4)
    
    def add(num1, num2):
        try:
            text.pop() # NameError, TypeError, eyError, SyntaxError, IndexError
        except AttributeError:
            print('AHHHHHH')
        else:
            print("no errors!")
        finally:
            print('error handling complete')
        return text 

math(10, 11)

# reassign a nonlocal variable
# any input/output operation
# mutation
# exception
# calling a function that has a side effect
