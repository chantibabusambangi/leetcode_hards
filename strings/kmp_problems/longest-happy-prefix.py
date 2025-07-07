'''
A string is called a happy prefix if is a non-empty prefix which is also a suffix (excluding itself).
Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.
'''
#as told in kmp we need to find lps array only # #easy_question
def get_lps(pattern):
      n=len(pattern)
      lps=[0]*len(pattern)
      i,j=1,0
      while(i<n):
          if(pattern[i]==pattern[j]):
              lps[i]=j+1
              j+=1
              i+=1
          elif(j!=0):
              j=lps[j-1]
          else:
              lps[i]=0
              i+=1
      return lps
  if(not s):
      return ""
  lps=get_lps(s)
  i=lps[-1]
  return s[:i]
