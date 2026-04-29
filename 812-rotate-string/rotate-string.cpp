class Solution {
public:
    bool rotateString(string s, string goal) {
    if (s.length() != goal.length()) {
        return false;
    }
    
    string combined = s + s;
    
    return combined.find(goal) != string::npos;
}
};