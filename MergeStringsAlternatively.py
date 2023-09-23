class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        r = []
        i = 0
        while i < len(word1) or i < len(word2):
            if i < len(word1):
                r.append(word1[i])
            if i < len(word2):
                r.append(word2[i])
            i += 1
        return ''.join(r)
