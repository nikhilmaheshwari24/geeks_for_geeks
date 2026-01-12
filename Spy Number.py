# https://www.geeksforgeeks.org/problems/spy-number/

class Solution:
    def checkSpy(self, n):
        # code here
        add=0
        multiply=1
        for i in str(n):
            add+=int(i)
            multiply*=int(i)
        return add == multiply
