'''
Given a string s, consider all duplicated substrings: (contiguous) substrings of s that occur 2 or more times. The occurrences may overlap.
Return any duplicated substring that has the longest possible length. If s does not have a duplicated substring, the answer is "".
'''
#idea is brute_force: checking each substring occurances>1 or not =>O(n3) 
#binary search +rabin karp
 def longestDupSubstring(self, s: str) -> str:
  #binary search with rabin karp
  #validate does the length 'mid' exist atleast twice
  def count(mid): #bool,chunk will be returened
      print(mid,end=",")
      #chunks of size=mid any chunk appears twice or more
      if(mid==len(s) or mid==0):
          return (False,"")
      p=256
      MOD = 2**31-1
      hashes=defaultdict(list)
      val=0
      for i in range(mid):
          val*=p
          val+=ord(s[i])-ord('a')+1
          val=val%MOD
      hashes[val].append(0)
      power=pow(p,mid-1,MOD)
      for i in range(mid,len(s)):
          val = (val - (power * (ord(s[i - mid]) - ord('a') + 1)) % MOD + MOD) % MOD
          val = (val * p + (ord(s[i]) - ord('a') + 1)) % MOD
          if(val in hashes):
              for start in hashes[val]:
                  if s[start:start + mid] == s[i - mid + 1:i + 1]:
                      print("yes")
                      #self.res=s[i-mid+1:i+1]
                      return (True,s[i-mid+1:i+1])
          hashes[val].append(i-mid+1)
      return (False,"")
  res=""
  l=1
  r=len(s)-1
  while(r>=l):
      mid=(l+r)//2
      flag,ans=count(mid)
      if(flag):
          res=ans
          l=mid+1
      else:
          r=mid-1
  return res
