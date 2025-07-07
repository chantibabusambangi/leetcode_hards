#using the lps the table we can do the search of a pattern(needle) on the string haystack
#(if you know how to find lps table its ok, else knowing the lps is the prerequsite)
#3cases overhere :
#if match increment i,j and check if j==len(needle) =>match was found
#mismatch=> if(j!=0) j=lps[j-1] else:i+1
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
          #wait for pre-fix to hit
          j=lps[j-1]
      else:
          lps[i]=0
          i+=1
  return lps
lps=get_lps(needle)
i,j=0,0
while(i<len(haystack)):
  if(haystack[i]==needle[j]):
      i+=1
      j+=1
      if(j==len(needle)):
          #match was found
          return i-j #is the index
  elif(j!=0):
      j=lps[j-1]
  else:
      i+=1
return -1 #not found
