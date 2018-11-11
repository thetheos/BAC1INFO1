def compose(f, g):
    def h(x):
        return f(g(x))
    return h

#Or
def compose(f, g):
    return lambda x : f(g(x))