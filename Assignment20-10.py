def anagram(s1,s2):
    if len(s1)==len(s2):
        for i in s1:
            if s1.count(i)!=s2.count(i):
                print("not anagram")
                break
        else:
            print("it is anagram")
