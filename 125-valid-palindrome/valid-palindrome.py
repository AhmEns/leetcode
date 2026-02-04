class Solution(object):
    def isPalindrome(self, s):
        cleaned = "".join(char for char in s.lower() if char.isalnum())
        
        if cleaned == cleaned[::-1]:
            return True
        else:
            return False

