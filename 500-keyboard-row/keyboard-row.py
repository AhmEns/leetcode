class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        row_1 = "qwertyuiopQWERTYUIOP"
        row_2 = "asdfghjklASDFGHJKL"
        row_3 = "zxcvbnmZXCVBNM"
        i = 0
        j = 0
        result = []

        for n in words:
            if n[i] in row_1:
                for x in n:
                    if not x in row_1:
                        j = j + 1
                if j == 0:
                    result.append(n)
            elif n[i] in row_2:
                for x in n:
                    if not x in row_2:
                        j = j + 1
                if j == 0:
                    result.append(n)
            elif n[i] in row_3:
                for x in n:
                    if not x in row_3:
                        j = j + 1
                if j == 0:
                    result.append(n)
            j = 0
        return result