class Solution:
    def isPalindrome(self, s: str) -> bool:
        #preprocess input     
        new_s = ''.join(c.lower() for c in s if self.alphaNum(c))
        print(new_s)
        slen = len(new_s)
        left, right = 0, slen-1 #pointing at each end of the string
        while(left < right):
            if new_s[left] != new_s[right]:
                return False
            left += 1
            right -= 1

        return True

    def alphaNum(self, c):
        return ord('a')<=ord(c)<=ord('z') or ord('A')<=ord(c)<=ord('Z') \
        or ord('0')<=ord(c)<=ord('9')