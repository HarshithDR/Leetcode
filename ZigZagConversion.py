class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        str =''
        if numRows == 1 or numRows >= len(s):
            return s

        result = [[] for i in range(numRows)]
        row, jump = 0, 1

        for char in s:
            result[row].append(char)
            if row == 0:
                jump = 1
            elif row == numRows - 1:
                jump = -1
            row += jump
            
        for x in range(len(result)):
            for y in range(len(result[x])):
                str += result[x][y]
        return str
