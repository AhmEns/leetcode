class Solution(object):
    def isPerfectSquare(self, num):
        sol = 1
        sag = num
        while sol <= sag:
            orta = (sol + sag) // 2
            kare = orta * orta

            if kare == num:
                return True
            elif kare < num:
                sol = orta + 1
            else:
                sag = orta - 1
        return False