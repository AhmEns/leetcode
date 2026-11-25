class Solution(object):
    def pivotInteger(self, n):
        bas, son = 1, n
        basToplam, sonToplam = 1, n
        
        while bas < son:
            if basToplam < sonToplam:
                bas += 1
                basToplam += bas
            else:
                son -= 1
                sonToplam += son
                
        return bas if basToplam == sonToplam else -1