# https://www.geeksforgeeks.org/problems/fizz-buzz/

class Solution:
    def fizzBuzz(self, n : int):
        # code here
        qlist=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                qlist.append("FizzBuzz")
            elif i%3==0:
                qlist.append("Fizz")
            elif i%5==0:
                qlist.append("Buzz")
            else:
                qlist.append(str(i))
        return qlist
