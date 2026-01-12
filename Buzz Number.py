# https://www.geeksforgeeks.org/problems/buzz-number/

class Solution:
    def isBuzz(self, n):
        # code here
        return n % 7 == 0 or str(n).endswith('7')
