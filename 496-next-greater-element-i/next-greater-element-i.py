class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        ans = []

        for num in nums1:
            i = nums2.index(num)
            greater = -1

            for j in range(i + 1, len(nums2)):
                if nums2[j] > num:
                    greater = nums2[j]
                    break

            ans.append(greater)

        return ans