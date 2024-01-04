# 238. Product of Array Except Self
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

# You must write an algorithm that runs in O(n) time and without using the division operation.

 

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [24,12,8,6]
# Example 2:

# Input: nums = [-1,1,0,-3,3]
# Output: [0,0,9,0,0]
 

# Constraints:

# 2 <= nums.length <= 105
# -30 <= nums[i] <= 30
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #better memory
        n = len(nums)
        result = [0] * n
        result[0] = 1

        for i in range (1,n):
            result[i] = result[i-1] * nums [i-1]
        
        right_product = 1
        for i in range (n-1, -1, -1):
            result[i] *=right_product
            right_product *= nums[i]
        
        return result

        #faster approach
        # n = len(nums)
        # rightArr = [0] * n
        # leftArr = [0] * n
        # result = [0] * n

        # leftArr[0] = 1
        # rightArr[n-1] = 1

        # for i in range (1, n):
        #     leftArr[i] = leftArr [i-1] * nums [i-1]
        
        # for i in range (n-2, -1, -1):
        #     rightArr[i] = rightArr[i+1] * nums[i+1]
        
        # for i in range (n):
        #     result[i] = leftArr[i] * rightArr[i]
        
        # return result


def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Test input array
    nums = [1, 2, 3, 4]

    # Call the productExceptSelf method using the instance and provided array
    result = solution.productExceptSelf(nums)

    # Display the result
    print("The product of array except self:", result)

if __name__ == "__main__":
    main()