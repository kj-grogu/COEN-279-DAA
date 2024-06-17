class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        # from the start and end, always try to sum the lower side
        st, en = 0, len(nums)-1
        count = 0
        while st <= en:
            if nums[st] == nums[en]:
                st += 1
                en -= 1
                continue
            count += 1
            if nums[st] < nums[en]:
                nums[st+1] += nums[st]
                st += 1
            else:
                nums[en-1] += nums[en]
                en -= 1
        
        return count