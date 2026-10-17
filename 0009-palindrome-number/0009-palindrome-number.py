class Solution(object):
    def isPalindrome(self, s):
        if s<0:
            return False
        temp=s
        rem=0
        res=0
        while temp>0:
            rem=temp%10
            res=res*10+rem
            temp=temp//10
        if res==s:
            return True
        else:
            return False
        