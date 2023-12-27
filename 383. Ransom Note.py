# 383. Ransom Note

# Given two strings ransomNote and magazine, return true if ransomNote can be constructed by using the letters from magazine and false otherwise.

# Each letter in magazine can only be used once in ransomNote.
 
# Example 1:

# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:

# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:

# Input: ransomNote = "aa", magazine = "aab"
# Output: true

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arrMag = [char for char in magazine]
        arrRan = [char for char in ransomNote]
        x = 0
        if arrMag == [] and arrRan == []:
            return True
        elif arrMag != [] and arrRan == []:
            return False
        elif (len(arrMag)) < (len(arrRan)):
            return False
        else:
            while x <= (len(arrMag)-1):
                i = 0
                while i <= (len(arrRan)-1):
                    if arrRan[i] == arrMag[x]:
                        arrRan.pop(i)
                        arrMag.pop(x)
                        x-=1
                        if arrRan == []:
                            return True
                        elif arrRan == arrMag:
                            return True
                    else:
                        i+=1
                x += 1            
            return False

def main():
    # Create an instance of the Solution class
    solution = Solution()

    # Define your ransom note and magazine strings
    ransom_note = "ce"
    magazine = "e"

    # Call the canConstruct function using the instance and provided strings
    result = solution.canConstruct(ransom_note, magazine)

    # Display the result
    if result:
        print("Ransom note can be constructed from the magazine.")
    else:
        print("Ransom note cannot be constructed from the magazine.")

if __name__ == "__main__":
    main()