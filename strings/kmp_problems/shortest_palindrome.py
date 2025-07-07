'''
You are given a string s. You can convert s to a palindrome by adding characters in front of it.
Return the shortest palindrome you can find by performing this transformation.
'''
#take your time and analyse the problem.
#we want nothing but longest palindrome starts from index 0 i.e = longest prefix palindrome
#for this we find lps, not for s, to temp= s+ '#'+ reversed(s) '#' chars avoids overlap
#and the last value of lps table will give you the longest prefix palindrome
def get_lps(pattern):
    n=len(pattern)
    lps=[0]*n
    i,j=1,0
    while(i<n):
        if(pattern[i]==pattern[j]):
            lps[i]=j+1
            j+=1
            i+=1
        elif(j!=0):
            #let we wiat from pre-fix
            j=lps[j-1]
        else:
            lps[i]=0
            i+=1
    return lps
temp=s+'#'+s[::-1]
lps=get_lps(temp)
lpp=lps[-1]
added=s[lpp:]
return added[::-1]+s

        
