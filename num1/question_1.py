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
