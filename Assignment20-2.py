def isprime(n):
    for i in range(2,n):
        if n%i==0:
            return"not prime"
    else:
        return"prime number"

n=int(input("Enter a number:"))
p=isprime(n)
print(p)
