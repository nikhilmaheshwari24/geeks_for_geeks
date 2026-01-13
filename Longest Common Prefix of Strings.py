# https://www.geeksforgeeks.org/problems/longest-common-prefix-in-an-array5129/

class Solution:
    def longestCommonPrefix(self, arr):
        # code here
        prefix = arr[0]
        
        for word in arr[1:]:
            while not word.startswith(prefix):
                prefix = prefix[:-1]
                if prefix == "":
                    return ""
        return prefix
