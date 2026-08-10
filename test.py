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