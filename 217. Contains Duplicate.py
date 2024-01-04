# 217. Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

 

# Example 1:

# Input: nums = [1,2,3,1]
# Output: true
# Example 2:

# Input: nums = [1,2,3,4]
# Output: false
# Example 3:

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False


def main():
    # Creating an instance of the Solution class
    solution = Solution()

    # Test list of numbers
    test_nums = [2,14,18,22,22]  # Replace this list with your test data

    # Call the containsDuplicate function using the instance and provided list
    has_duplicate = solution.containsDuplicate(test_nums)

    # Display the result
    if has_duplicate:
        print("The list contains duplicate elements.")
    else:
        print("The list does not contain any duplicates.")

if __name__ == "__main__":
    main()
