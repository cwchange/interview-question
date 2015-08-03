"""
6. Write a method that finds the largest sum of consecutive entries in an array given a group size.  It should take an
array and the interval size as inputs and should return both the largest sum and the index of the first entry in the
group. For example, in the following Array [1,1,1,1,1,1,1,2] given a group size of 2 the result would be a maximum sum of
3 and a position of 6.

"""


class q_6:
       def __init__(self, array, size):
             self.size=size
             self.array=array
             self.sum=0
             self.position=0
             self.n=len(array)-self.size+1
 
       def interval(self):
             for i in xrange(self.n):
                   temp=self.array[i:self.size]
                   self.size+=1
                   if (sum(temp) > self.sum):
                        self.sum=sum(temp)
                        self.position=i
 
if __name__ == "__main__":
        temp=[1,1,1,1,1,1,1,2]
        first=q_6(temp, 2)
        first.interval()
        print [first.sum, first.position]
 
        temp_2=[3,2,105,2,3,5,2,3,4,6,7,4,7,9,0,4,5,8,67,1,23,8,9,5,3,4,5,6,8,7,9,7,4,3,9,4,5,67]
        second=q_6(temp_2, 3)
        second.interval()
        print [second.sum, second.position]
