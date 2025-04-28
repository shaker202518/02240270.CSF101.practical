class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        return len(set(nums))!=len(nums)

# Python Program check if there are any duplicates  
# in the array using Hashing

def checkDuplicates(arr):
    n = len(arr)

    # Create a set to store the unique elements
    st = set()

    # Iterate through each element
    for i in range(n):
        
        # If the element is already present, return true
        # Else insert the element into the set
        if arr[i] in st:
            return True
        else:
            st.add(arr[i])

    # If no duplicates are found, return false
    return False

if __name__ == "__main__":
    arr = [4, 5, 6, 4]
    print(checkDuplicates(arr))
    
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        return (len(set(count)) == 1 and list(set(count))[0] == 0)


# Using hash Map or Dictionary

# Python Code to check if two Strings are anagram of 
# each other using Dictionary

def areAnagrams(s1, s2):
    
    # Create a hashmap to store character frequencies
    charCount = {}
    
    # Count frequency of each character in string s1
    for ch in s1:
        charCount[ch] = charCount.get(ch, 0) + 1
  
    # Count frequency of each character in string s2
    for ch in s2:
        charCount[ch] = charCount.get(ch, 0) - 1
  
    # Check if all frequencies are zero
    for value in charCount.values():
        if value != 0:
            return False
    
    # If all conditions satisfied, they are anagrams
    return True

if __name__ == "__main__":
    s1 = "geeks"
    s2 = "kseeg"
    print("true" if areAnagrams(s1, s2) else "false")

