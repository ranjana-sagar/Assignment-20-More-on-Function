def square(n):
    x=[i*2 for i in range(1,n+1)]
    print(x)

n=int(input("Enter a number:"))
x=square(n)#function call
print(x)
