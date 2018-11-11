import time
from functools import wraps


def time_it(f):
    #we could put *args instead of x to handle the case when the function f has multiple parameters
    t1 = 0
    t0 = 0
    def wrapped(x):
        t0 = time.clock()
        result = f(x)
        t1 = time.clock()
        print("ellapsed time: {0}".format(t1-t0))
        return result
    return wrapped,t1-t0


def fib_rec(n):
    """
      Computes numbers in the Fibonacci sequence 0, 1, 1, 2, 3, 5, 8, 13, 21, ...
      pre:  'n' is natural number (an integer >= 0)
      post: returns the n-th Fibonacci number,
            where fib(0) = 0 and fib(1) = 1
            and any other Fibonacci number is defined
            as the sum of the previous 2 Fibonacci numbers,
            for example: fib(2) = fib(0) + fib(1) = 0 + 1 = 1
    """
    if n <= 1:
        return n
    t = fib_rec(n-1) + fib_rec(n-2)
    return t


def fib_it(n):
    a,b,c=0,1,0
    for i in range(n-1):
        c = b+a
        a = b
        b = c    
    return c


def time_dif_fibo(n):
    print("The time difference to compute the {0}'th term is: {}s".format())

#print(time_it(fib))
r = time_it(fib_rec)
result = r[0](20)
time = r[1]
print(result,time)
time_it(fib_it)[0](20)


#print("the result: {0} has been computed in {1:.2f}s".format(n,t1-t0))