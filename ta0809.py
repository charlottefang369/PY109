# TA session with Pete (8/9 @7AM)



# What is the output of this code? Explain why, and what concepts it demonstrates.

greeting = "Hello"

def greet(greeting):
    greeting += " world"
    print(greeting)

greet(greeting)
print(greeting)



# What is the output of this code? Explain why, and what concepts it demonstrates.

greeting = "Hello"

def greet():
    greeting += " world"
    print(greeting)

greet()
print(greeting)



# Q: What does this output? Why?
def foo():
    x = 'foo'

    def bar():
        x = 'bar'
        print(x) 

    def baz():
        print(x) 

    bar()
    baz()

foo()



# Q: What do we mean by the term "pass by object reference"?


def foo(string):
    return string + string

foo("hello")    

result = foo("hello")




# Q: What will the following code print? How did you arrive at your answer?

players = [
  {'name': "Joe", 'age': 25},
  {'name': "Andy", 'age': 31},
]

new_team = players
last_years_team = players[:]

for player in last_years_team:
    player['age'] += 1 #age + 1 reflects in all three varibles

new_team.append({
    'name': 'Bob',
    'age': 19,    # + element for new team and player, not last years team
})

print("players:", players)
print("new_team:", new_team)
print("last_years_team:", last_years_team)