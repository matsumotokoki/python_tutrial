for n in range(2,101):
    for x in range(2,n):
        if n%x==0:
            print(n,' is not prime number')
            break
    else:
        print(n,' is prime number')
