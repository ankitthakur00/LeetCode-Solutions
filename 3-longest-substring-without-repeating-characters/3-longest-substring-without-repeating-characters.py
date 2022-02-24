class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic={}
        start=0
        max_len=0
    
        for i in range(len(s)):
            if s[i] in dic.keys():
                start=max(start,dic[s[i]]+1)
        
            dic[s[i]]=i
            max_len=max(i-start+1,max_len)
        return max_len;