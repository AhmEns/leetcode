class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        first_capital = word[0].isupper()
        all_capital = True
        all_lower = True

        for i in range(len(word)):
            if word[i].isupper():
                all_lower = False
            else:
                all_capital = False
            if word[i].isupper() and i != 0:
                first_capital = False

        return all_lower or all_capital or first_capital
        