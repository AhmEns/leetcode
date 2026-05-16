#include <iostream>
#include <string>

class Solution {
public:
    int numJewelsInStones(std::string jewels, std::string stones) {
        int count = 0;
        
        for (char stone : stones) {
            for (char jewel : jewels) {
                if (stone == jewel) {
                    count++;
                    break;
                }
            }
        }
        
        return count;
    }
};