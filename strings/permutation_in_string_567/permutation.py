# leetcode - 567

def checkperm(self, s1, s2):
  if len(s1) > len(s2):
    return 0
  nums1 = [0]*26
  nums2 = [0]*26
  
  for char in s1:
    nums1[ord(char) - ord('a')] += 1 #add 1 for each character in s1
  for ch in range(0,len(s2)):
    nums2[ord(s2[ch] - ord('a')] += 1 # add 1 for each character in s2
    if ch >= len(s1) - 1:
        if nums1 == nums2:
              return 1
        nums2[ord(s2[ch - len(s1) + 1] - ord('a')] -= 1 # subtract 1 from prev index
  return 0
