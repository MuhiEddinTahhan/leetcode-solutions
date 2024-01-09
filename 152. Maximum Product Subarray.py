# 152. Maximum Product Subarray
# Given an integer array nums, find a 
# subarray
#  that has the largest product, and return the product.

# The test cases are generated so that the answer will fit in a 32-bit integer.

 

# Example 1:

# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:

# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
 

# Constraints:

# 1 <= nums.length <= 2 * 104
# -10 <= nums[i] <= 10
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        current_max = current_min = total_max = nums[0]
        for i in range (1,len(nums)):
            if nums[i] < 0:
                current_max, current_min = current_min, current_max
            current_max = max(nums[i], current_max * nums[i])
            current_min = min(nums[i], current_min * nums[i])
            total_max = max(current_max, total_max)

        return total_max

def main():
    # Example usage:
    solution = Solution()
    nums = [-4,-3,-2]
    result = solution.maxProduct(nums)
    print(f"The maximum product of two integers in the list is: {result}")

if __name__ == "__main__":
    main()