# https://www.geeksforgeeks.org/problems/non-repeating-character-1587115620/

class Solution:
    def nonRepeatingChar(self,s):
        #code here
        qdict={}
        for i in str(s):
            qdict[i]=qdict.get(i,0)+1
        for k,v in qdict.items():
            if v < 2:
                return k
        return "$"
