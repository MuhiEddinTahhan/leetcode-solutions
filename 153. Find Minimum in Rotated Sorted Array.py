# 153. Find Minimum in Rotated Sorted Array
# Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

# [4,5,6,7,0,1,2] if it was rotated 4 times.
# [0,1,2,4,5,6,7] if it was rotated 7 times.
# Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

# Given the sorted rotated array nums of unique elements, return the minimum element of this array.

# You must write an algorithm that runs in O(log n) time.

class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) -1
        while left < right:
            mid = (left+right)//2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
        return nums[left]


def main():
    # Example usage:
    solution = Solution()
    nums = [4, 5, 6, 7, 0, 1, 2]
    minimum = solution.findMin(nums)
    print(f"The minimum element in the rotated sorted array is: {minimum}")

if __name__ == "__main__":
    main()