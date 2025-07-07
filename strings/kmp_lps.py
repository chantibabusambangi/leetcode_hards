#lps longest prefix suffix table/array
#ex. pattern="abcababc"
#    lps=[0,0,0,1,2,1,2,3]
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
