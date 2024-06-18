from typing import List

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        st, en = 0, len(nums) - 1  # Initialize pointers to the start and end of the list
        count = 0  # Initialize the operation count
        
        while st <= en:
            if nums[st] == nums[en]:
                # If the elements at both pointers are equal, move both pointers inward
                st += 1
                en -= 1
            else:
                count += 1  # Increment the operation count
                if nums[st] < nums[en]:
                    # If the element at the start is smaller, merge it with the next element
                    nums[st + 1] += nums[st]
                    st += 1
                else:
                    # If the element at the end is smaller, merge it with the previous element
                    nums[en - 1] += nums[en]
                    en -= 1
        
        return count  # Return the total number of operations

# Example usage

