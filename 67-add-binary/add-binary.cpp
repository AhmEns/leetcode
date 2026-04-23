class Solution {
public:
    string addBinary(string a, string b) {
        int i = a.length() - 1;
        int j = b.length() - 1;
        int carry = 0;
        
        string res = "";
        
        while (i >= 0 || j >= 0 || carry) {
            int sum = carry;
            
            if (i >= 0) {
                sum += (a[i] == '1' ? 1 : 0);
                i--;
            }
            if (j >= 0) {
                sum += (b[j] == '1' ? 1 : 0);
                j--;
            }
            
            char currentBit = (sum % 2 == 0 ? '0' : '1');
            res = currentBit + res; 
            
            carry = sum / 2;
        }
        
        return res;
    }
};