class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        letters = [
            'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
        ]
        morse_codes = [
            ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", 
            ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", 
            "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."
        ]
        morse_words = []
        word = ""
        return_val = 0
        for i in words:
            for j in i:
                for k in range(len(letters)):
                    if letters[k] == j:
                        word += morse_codes[k]
            if word not in morse_words:
                return_val += 1
                morse_words.append(word)
            word = ""
        return return_val
