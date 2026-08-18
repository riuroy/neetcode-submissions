class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        lookup_table = [0] * 26
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            lookup_table[ord(s[i])-ord('a')]+=1;
            lookup_table[ord(t[i])-ord('a')]-=1;
        
        for i in lookup_table:
            if i !=0:
                return False
        return True;
        
