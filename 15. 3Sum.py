# 15. 3Sum
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

 

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.
# Example 2:

# Input: nums = [0,1,1]
# Output: []
# Explanation: The only possible triplet does not sum up to 0.
# Example 3:

# Input: nums = [0,0,0]
# Output: [[0,0,0]]
# Explanation: The only possible triplet sums up to 0.
 

# Constraints:

# 3 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        goal = []
        for i in range (len(nums)-2):
            if nums[i] == nums [i-1] and i>0:
                continue
            target = -nums[i]
            left, right=i+1, len(nums)-1

            while left < right:
                current_sum = nums[left]+nums[right]
                if current_sum == target:
                    goal.append([nums[right], nums[left],nums[i]])
                    left +=1
                    right-=1
                
                    while left < right and nums[left] == nums[left-1]:
                        left+=1
                    while left < right and nums[right] == nums[right+1]:
                        right-=1
                elif current_sum < target:
                    left+=1
                else:
                    right-=1
        return goal

    

def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Example 1
    nums1 = [-1, 0, 1, 2, -1, -4]
    result1 = solution.threeSum(nums1)
    print("Example 1:")
    print(result1)

    # Example 2
    nums2 = [0, 1, 1]
    result2 = solution.threeSum(nums2)
    print("\nExample 2:")
    print(result2)

    # Example 3
    nums3 = [0, 0, 0]
    result3 = solution.threeSum(nums3)
    print("\nExample 3:")
    print(result3)

if __name__ == "__main__":
    main()