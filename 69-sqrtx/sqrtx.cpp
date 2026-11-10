class Solution {
public:
    int mySqrt(int x) {
        int y = 1;

        while (y <= x / y){
            y++;
        }
        return y - 1;

    }
};