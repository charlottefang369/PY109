# Question 1: 
# Write a function find_common_elements that takes two lists as arguments. 
# It should return a new list containing the elements 
# that are common to both input lists, with no duplicates. 
# The order of elements in the returned list does not matter. 

# Solution 1:
def find_common_elements(lst1, lst2): 
    result = [] 

    for number in lst1: 
        for num in lst2: 
            if number == num: 
                result.append(number) 

    return list(set(result))

# Solution 2:
def find_common_elements(lst1, lst2): 
    result = [] 

    for number in lst1:
        if number in lst2 and number not in result: 
            result.append(number) 

    return result 
                
# Test cases: 
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(find_common_elements(list1, list2)) # [4, 5] or [5, 4]

list3 = ['a', 'b', 'c', 'a']
list4 = ['d', 'c', 'a', 'e']
print(find_common_elements(list3, list4)) # ['a', 'c'] or ['c', 'a']

list5 = [1, 2, 3]
list6 = [4, 5, 6]
print(find_common_elements(list5, list6)) # []



# Question 2: 
# Write a function run_simulation that simulates a simple process. 
# It should have a variable time_elapsed initialized to 0. 
# Inside run_simulation, define a nested function tick that increments 
# time_elapsed by 1 and prints the new time. 
# The run_simulation function should then call tick three times.

# Solution 1: 
def run_simulation(): 
    def tick(): 
        time_elapsed = 0 
        for _ in range(3): 
            time_elapsed += 1 
            print(time_elapsed)
    tick()

run_simulation()

# Solution 2: 
def run_simulation(): 
    time_elapsed = 0 
    
    def tick(): 
        for _ in range(3):
            nonlocal time_elapsed
            time_elapsed += 1 
            print(time_elapsed)
    
    tick()

run_simulation()

# Solution 3: 
def run_simulation(): 
    time_elapsed = 0 
    
    def tick(): 
        nonlocal time_elapsed
        time_elapsed += 1 
        print(time_elapsed)
    
    tick()
    tick()
    tick()

run_simulation()




# Question 3:What will below code output and why? 

numbers = [1, 2, 3]
number_enthusiast = 'Lisa Simpson'

for num in numbers:
    sentence = number_enthusiast + f" loves the number {num}!"
    print(sentence)

print(num)


# After the loop finishes, the program proceeds to print(num).
# This is the key line. In many other languages, variables declared inside a block 
# (like a for loop) are local to that block and cannot be accessed from outside. 
# If Python had block scope, the variable num would cease to exist after the 
# loop terminated, and line 8 would raise a NameError.
# However, the code executes line 8 without an error and prints 3. 
# This is because the variable num, which was assigned its values within the loop, 
# is actually part of the surrounding scope (in this case, the global scope). 
# It remains accessible after the loop is complete and holds the last value 
# assigned to it during the final iteration.
# This behavior demonstrates that loops and other blocks like if statements 
# do not create a new local scope in Python. 
# Variables defined within them are accessible in the scope where the block
# itself resides.


# Question 4: 
# Write a function that takes a list of numbers 
# and returns the sum of the sums of each leading subsequence in that list.


# input: list 

# requirement: 
# [3, 5, 2]
# 3
# 3 + 5
# 3 + 5 + 2


# return: sum 
# [3, 5, 2]

def sum_of_sums(numbers):
    final_result = []
    result = 0
    for num in numbers: 
        result = result + num 
        final_result.append(result)
    # 3 result = 0 + 3 = 3
    # 5 result = 3 + 5 = 8
    # 2 result = 8 + 2 = 10 

    return sum(final_result)

    
# The argument will always be a list of numbers.
print(sum_of_sums([3, 5, 2]) == 21)
# (3) + (3 + 5) + (3 + 5 + 2) --> 3 + 8 + 10 --> 21

print(sum_of_sums([1, 5, 7, 3]) == 36)
# (1) + (1 + 5) + (1 + 5 + 7) + (1 + 5 + 7 + 3) --> 1 + 6 + 13 + 16 --> 36

print(sum_of_sums([4]) == 4)
print(sum_of_sums([1, 2, 3, 4, 5]) == 35)
