def my_fun(arg1,*argv):
    print("first argument:",arg1)
    for arg in argv:
        print("next argument through *argv:",arg)


my_fun('hello','welcome','to','python')


def my_func(**kwargs):
    for key,value in kwargs.items():
        print ("%s == %s" % (key, value))

my_func(first='B', mid='to', last='C')

#ex
fib = lambda n : n if n<= 1 else fib(n-1) + fib(n-2)
result = fib(10)
print(result)


def sir(n):
    a,b = 0,1
    for i in range(n):
        print(a,end="")
        a,b = b,a+b
sir(55)


def afiseaza_55():
    return 5*11
print(afiseaza_55())

def suma():
    return sum(range(1,11))

print(suma())