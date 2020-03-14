import sys
if(len(sys.argv)<3):
    print('Error')
else:
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    ans = True
    if len(s2) < len(s1):
        ans = False
    else:
        one = {}
        two = {}
        for c in s1:
            if c in one:
                one[c] = one[c]+1
            else:
                one[c] = 1

        for c in s2:
            if c in two:
                two[c] = two[c]+1
            else:
                two[c] = 1

        for k1,v1 in one.items():
            for k2,v2 in two.items():
                if v1 == v2 :
                    one[k1] = 0
                    two[k2] = 0
                    break

        for val in one.values():
            if val > 1 :
                ans = False

    print(ans)
