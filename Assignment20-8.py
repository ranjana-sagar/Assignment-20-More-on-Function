def count(s1):
    l,u=0,0
    for i in s1:
        if ord(i)in range(97,123):
            l+=1
        elif ord(i)in range(65,91):
            u+=1
    print("Total Upper letter=",u,", Total lower letter=",l)        
            
