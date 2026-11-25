class Solution(object):
    def pivotInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        bas, son, basToplam, sonToplam, constN = 1, n, 0, 0, n

        while n > 0:
            while bas <= n:
                basToplam += bas
                bas += 1
            while son >= n:
                sonToplam += son
                son -= 1
            if basToplam == sonToplam:
                return n
            bas, son, basToplam, sonToplam= 1, constN, 0, 0
            n -= 1
        return -1