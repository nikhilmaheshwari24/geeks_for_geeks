# https://www.geeksforgeeks.org/problems/count-even-letters/

class Solution:
    def count(self, s):
        # code here
        qdict={}
        for i in str(s):
            qdict[i]=qdict.get(i,0)+1
        qlist=[]
        for i,j in qdict.items():
            if j%2==0:
                qlist.append(j)
        return len(qlist)
