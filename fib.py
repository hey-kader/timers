def main ():
        print (fib(500))




def fib(n):
    if n < 0:
        print ("incorrect input")
    elif n == 0:
        return 0
    elif n ==1 or n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

main ()
