class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=s.lower()
        g=list(l.replace(" ", ""))
        for i in g:
            if not i.isalnum():
                g.remove(i)
        n=g[::-1]
        if g==n:
            return True
        else:
            return False