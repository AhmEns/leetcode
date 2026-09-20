class Solution(object):
    def buddyStrings(self, s, goal):
        """
        :type s: str
        :type goal: str
        :rtype: bool
        """
        dif = 0
        dif_list = []
        if len(s) != len(goal):
            return False
        if s == goal:
            return len(set(s)) < len(s)

        for i in range(len(s)):
            if s[i] != goal[i]:
                dif += 1
                dif_list.append(i)
        
        if dif == 2:
            return s[dif_list[0]] == goal[dif_list[1]] and s[dif_list[1]] == goal[dif_list[0]]
                
        return False