import timeit
def fib (n):
    a, b = 1, 2
    li = [] 
    li.append(a)
    li.append(b)
    begin = timeit.timeit()
    while n > 1:
        print (a, ' ',b,end=' ')
        a, b = b, a+b
        n-=1
        li.append(a)
        li.append(b)
    end = timeit.timeit()
    print ("time: ",end)

def main ():
    fib(5000)
main ()

