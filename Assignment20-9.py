def pangram(s1):
    s1=s1.lower()
    alphabet='abcdefghijklmnopqrstuvwxyz'
    for i in alphabet:
        if i not in s1:
            print("not pangram")
            break
    else:
        print("it is pangram")
        
