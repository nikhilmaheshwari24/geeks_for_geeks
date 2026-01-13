# https://www.geeksforgeeks.org/problems/consecutive-elements2306/

class Solution:
    def removeConsecutiveCharacter(self, s):
        # code here
        qlist=[s[0]]
        
        for ch in s:
            if ch!=qlist[-1]: # last element always getting updated
                qlist.append(ch)
        return "".join(qlist)
        
        
