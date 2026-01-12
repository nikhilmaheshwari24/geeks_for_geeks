# https://www.geeksforgeeks.org/problems/special-integers/

from typing import List

class Solution:
    def specialIntegers(self, n : int, arr : List[int]) -> int:
        # code here
        se=set(arr) ## since distinct integer number was expected
        count=0 
        for i in se:
            if (i-1) in se and (i+1) in se:
                count+=1
        return count
