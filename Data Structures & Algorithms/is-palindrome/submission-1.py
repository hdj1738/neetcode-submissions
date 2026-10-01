class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        t=""
        for i in s:
            if ((ord(i)>96 and ord(i)<123) or ord(i)>=48 and ord(i)<=57):
                t+=i
        print(t)

        return t[::]==t[::-1]

        