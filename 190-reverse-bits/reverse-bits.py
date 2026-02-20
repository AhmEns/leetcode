class Solution(object):
    def reverseBits(self, n):
        bin_n = bin(n)[2:].zfill(32)
        reverse_bin = bin_n[::-1]
        return int(reverse_bin, 2)
        
        