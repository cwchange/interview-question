"""
1. Write a function that prints the numbers from 1 to 100. But for multiples of three print “Foo” instead of the number and for the multiples of five print “Bar”. For numbers which are multiples of both three and five print “FooBar”. Example output: 1 2 Foo 4 Bar Foo 7 8 Foo Bar 11 Foo 13 14 FooBar …
"""


#Solution to question 1
def out_print(num):
        temp=1
        while temp <=num:
             if (temp%15 == 0):
                  print 'FooBar',
                  temp+=1
             elif (temp%5 == 0):
                  print 'Bar',
                  temp+=1
             elif (temp%3 == 0):
                  print 'Foo',
                  temp+=1
             else:
                  print temp,
                  temp+=1
 
if __name__ == "__main__": out_print(100)
