"""
3. Given the following pseudo code, determine the range of possible values for “a” in your language of choice:

x = random_int(1,6)

y = random_int(1,6)

z = random_int(1,6)

a = x + y + z

"""





"""
For this question, by law of large number, if the number of trials increase, it will get close to the true mean.
"""
 
import random as rd
 
class q_3:
    def __init__(self):
        self.temp=[]
        self.lower=99999
        self.upper=0
 
    def value_a(self):
        x= rd.randint(1,6)
        y= rd.randint(1,6)
        c= rd.randint(1,6)
        a=x+y+c
        return a
 
    def interval(self, n):
        for i in xrange(n):
            temp_data=self.value_a()
            self.temp.append(temp_data)
            if (temp_data < self.lower):
                self.lower=temp_data
            if (temp_data > self.upper):
                self.upper=temp_data
 
if __name__ == "__main__":
        #For 10 trials
        first=q_3()
        first.interval(10)
        print '10 trials ==> ', [first.lower, first.upper]
 
       #For 100 trials
        second=q_3()
        second.interval(100)
        print '100 trials ==> ', [second.lower, second.upper]
 
        #for 1000 trials
        third=q_3()
        third.interval(1000)
        print '1000 trials ==> ', [third.lower, third.upper]
 
        #For 10000 trials
        fourth=q_3()
        fourth.interval(10000)
        print '10000 trials ==> ', [fourth.lower, fourth.upper]
