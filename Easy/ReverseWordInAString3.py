class Solution(object):
    def reverseWords(self, s):
        strArr = s.split()
        reverse_str = [word[::-1] for word in strArr]
        return ' '.join(reverse_str)
        