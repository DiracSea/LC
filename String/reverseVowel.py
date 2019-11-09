class Solution:
    def reverseVowels(self, s: str) -> str:
        vowel = 'aeiouAEIOU' 
        l = 0 
        r = len(s) - 1 
        s = list(s)
        while l <= r: 
            while l <= r and s[l] not in vowel: 
                l += 1 
            while l <= r and s[r] not in vowel: 
                r -= 1 
            if l > r: break
            s[l], s[r] = s[r], s[l]
            l, r = l + 1, r - 1
        return ''.join(s)