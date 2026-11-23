class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        alphabet = "abcdefghijklmnopqrstuvwxyz"
        noRepeat = []
        return_val = ""
        for i in range(len(key)):
            if key[i] not in noRepeat and key[i] != " ":
                noRepeat.append(key[i])
        for i in message:
            if i == " ":
                    return_val += " "
            for j in range(len(noRepeat)):
                if noRepeat[j] == i:
                    return_val += alphabet[j]

        return return_val