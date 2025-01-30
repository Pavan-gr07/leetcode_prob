# printing permutation sequence
# set = [a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,.....]

# if 3
# ['abc','acb','bac','bca','cab','cba']

# if 4
# ['a] 

def permutationString(s,chosen):
    if not s:
        print(chosen)
    else:
        for i in range(len(s)):
            char = s[i]
            permutationString(s[:i]+s[i+1:],chosen+char)


permutationString('123',"")
