class Solution:
    def isPalindrome(self, x: int) -> bool:
        if (x<0):
            return False
        
        s = 0
        i = x
        while (i>0):
            d = i % 10
            s = s * 10 + d
            i = i // 10     # imp point here - using integer division
            
        if ( x == s):
            return True
        return False