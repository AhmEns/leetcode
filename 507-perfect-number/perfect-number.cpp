class Solution {
public:
    bool checkPerfectNumber(int num) {
        int x = 1, sum = 0;
        while (x * x < num){
            if (num % x == 0){
                sum += x;
                sum += (num / x);
            }
            x++;
        }
        return sum == num * 2;
    }
};