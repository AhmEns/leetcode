class Solution(object):
    def numberOfLines(self, widths, s):
        """
        :type widths: List[int]
        :type s: str
        :rtype: List[int]
        """
        return_val = []
        width, line_count, char_index, char_width = 0, 0, 0, 0
        for i in s:
            char_index = ord(i) - ord("a")
            char_width = widths[char_index]

            if width + char_width > 100:
                line_count += 1
                width = 0
            width += char_width

        if width != 0:
            line_count += 1
            
        return_val.append(line_count)
        return_val.append(width)
        return return_val