'''
30. Substring with Concatenation of All Words
You are given a string s and an array of strings words. All the strings of words are of the same length.
A concatenated string is a string that exactly contains all the strings of any permutation of words concatenated.
For example, if words = ["ab","cd","ef"], then "abcdef", "abefcd", "cdabef", "cdefab", "efabcd", and "efcdab" are all concatenated strings. "acdbef" is not a concatenated string because it is not the concatenation of any permutation of words.
Return an array of the starting indices of all the concatenated substrings in s. You can return the answer in any order.
Example 1:
Input: s = "barfoothefoobarman", words = ["foo","bar"]
Output: [0,9]
'''
#idea is use hashing(rabin karp)
#rabin karp (instead eniter string checking)
#idea is hash the s
#h[0] means hash value 0 to len_word 
MOD=10**9+7
def give_hash(word):
    p=17
    
    val=0
    for i in word:
        val*=p
        val+=ord(i)-ord('a')+1
        val=val%MOD
    return val
word_hash=[]
word_len=len(words[0]) #length of each word
if(word_len*len(words)>len(s)):
    return []
for word in words:
    word_hash.append(give_hash(word))
h=[] #hash for s
val=0
p=17
word_count = Counter(word_hash)
num_words = len(words)
for i in range(word_len):
    val*=p
    val+=ord(s[i])-ord('a')+1
h.append(val)
for i in range(word_len,len(s)):
    outhash=ord(s[i-word_len])-ord('a')+1
    val-=(outhash)*(p**(word_len-1))
    val*=p
    val+=ord(s[i])-ord('a')+1
    val=val%MOD
    h.append(val)
res=[]
for start in range(word_len):
    seen = Counter()
    count = 0
    left = start
    for right in range(start, len(h), word_len):
        word = h[right]
        if word in word_count:
            seen[word] += 1
            count += 1
            while seen[word] > word_count[word]:
                seen[h[left]] -= 1
                count -= 1
                left += word_len
            if count == num_words:
                res.append(left)
        else:
            seen.clear()
            count = 0
            left = right + word_len
return res
