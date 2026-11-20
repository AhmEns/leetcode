class Solution {
    public int numIdenticalPairs(int[] nums) {
        int i, j;
        int return_val = 0;

        for(i = 0; i < nums.length; i++){
            for(j = i + 1; j < nums.length; j++)
                if(nums[i] == nums[j]){
                    return_val++;
                }
        }

        return return_val;
    }
}