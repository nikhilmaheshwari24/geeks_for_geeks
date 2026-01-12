# https://www.geeksforgeeks.org/problems/reverse-words-in-a-given-string5459/

class Solution:
    def reverseWords(self, s):
        # code here
        qlist=list(s.strip('.').split('.'))
        qstr=""
        for i in qlist[::-1]:
            if "" != i:
                qstr+=(i+".")
            else:
                continue
        return (qstr.rstrip('.'))
        
