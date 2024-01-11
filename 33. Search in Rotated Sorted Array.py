# 33. Search in Rotated Sorted Array
# There is an integer array nums sorted in ascending order (with distinct values).

# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

# Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

# You must write an algorithm with O(log n) runtime complexity.

 

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:

# Input: nums = [1], target = 0
# Output: -1

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        low = self.findMin(nums)
        rightSide = self.binarySearch(nums, low, (len(nums)-1), target)
        if rightSide!=-1:
            return rightSide
        else:
            leftSide= self.binarySearch(nums, 0, low-1, target)
            return leftSide
        


    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) -1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return left
    
    def binarySearch(self, nums: list[int],low, high, target) -> int:
        while low <=high:
            mid = (high+low)//2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return -1

    


def main():
    # Example usage:
    solution = Solution()
    nums = [4,5,6,7,0,1,2]
    x = 0
    minimum = solution.search(nums, x)
    print(f"The element {minimum}")

if __name__ == "__main__":
    main()