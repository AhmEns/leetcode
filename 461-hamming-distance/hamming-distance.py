class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        bin_x = bin(x)[2:]
        bin_y = bin(y)[2:]
        max_len = max(len(bin_x), len(bin_y))
        bin_x = bin_x.zfill(max_len)
        bin_y = bin_y.zfill(max_len)
        return_val = 0

        for i in range(max_len):
            if bin_x[i] != bin_y[i]:
                return_val += 1
        return return_val