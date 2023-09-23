class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        r = s.split()
        return ' '.join(r[::-1])
