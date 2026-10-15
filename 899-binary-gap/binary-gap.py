class Solution(object):
    def binaryGap(self, n):
        """
        :type n: int
        :rtype: int
        """
        n = bin(n)[2:]
        liste = []
        return_val = 0

        for i in range(len(n)):
            if n[i] == "1":
                liste.append(i)

        for i in range(1, len(liste)):
            if liste[i] - liste[i - 1] > return_val:
                return_val = liste[i] - liste[i - 1]
        
        return return_val