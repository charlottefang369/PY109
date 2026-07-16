def foo():
    def bar():
        a = 1
        return a

    bar() # BAR
    b = 2
    return b

print(foo())
