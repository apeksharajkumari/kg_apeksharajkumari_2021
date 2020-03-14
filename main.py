import sys
if(len(sys.argv)<3):
    print('Error')
else:
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    ans = True
    if len(s2) < len(s1):  #length constraint: s2 has to be longer than s1 for one-to-one mapping of s1
        ans = False
    else:
        one = {}
        two = {}
        for ch in s1:    #storing characters of s1 and their frequencies in a dictionary one
            if ch in one:
                one[ch] = one[ch]+1
            else:
                one[ch] = 1

        for ch in s2:    #storing characters of s2 and their frequencies in a dictionary two
            if ch in two:
                two[ch] = two[ch]+1
            else:
                two[ch] = 1

        for k1,v1 in one.items():   #check if frequencies of chars in s1 match that of chars in s2
            for k2,v2 in two.items():
                if v1 == v2 :
                    one[k1] = 0 #if freq matches, mapping is possible, change freq to 0 for both to show they are mapped
                    two[k2] = 0
                    break

        for val in one.values():
            if val > 1 :    #0 means mapped and 1 means mapping possible since length constraint is met
                ans = False #greater than 1 means one-to-one mapping of s1 to s2 not possible

    print(ans)
