def f1(l1):
    l1=list(set(l1))
    return l1

#funcion call
print("Enter the number sepreted by comman:")
l1=[eval(i) for i in input().split(',')]
l=f1(l1)
print(l)
