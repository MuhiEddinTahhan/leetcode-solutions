# 53. Maximum Subarray
# Given an integer array nums, find the 
# subarray
#  with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.
# Example 2:

# Input: nums = [1]
# Output: 1
# Explanation: The subarray [1] has the largest sum 1.
# Example 3:

# Input: nums = [5,4,-1,7,8]
# Output: 23
# Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        total_Max = 0
        total_Cur = 0
        if len(nums)==1:
            return nums[0]
        for i in range(len(nums)):
            if nums[i] >= 0:
                total_Max += nums[i]
                if i == len(nums)-1:
                    return total_Max
            else:
                total_Max = nums[0]
                break
        
        total_Max=nums[0]

        for i in range(len(nums)):
            if nums[i] <= 0:
                total_Max = max(total_Max,nums[i])
                if i == len(nums)-1:
                    return total_Max
            else:
                total_Max = nums[0]
                break
        for i in range(len(nums)):
            total_Cur = max(total_Cur, 0)
            total_Cur += nums[i]
            total_Max = max(total_Max, total_Cur)
        
        return total_Max
        

def main():
    solution = Solution()
    nums = [-2,1]  # Example array
    max_subarray_sum = solution.maxSubArray(nums)
    print(f"The maximum subarray sum is: {max_subarray_sum}")

if __name__ == "__main__":
    main()
