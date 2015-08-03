#Solution to question 1
def out_print():
       for i in range(1,1001):
             if (i%15 == 0):
                  print 'FooBar',
             elif (i%5 == 0):
                  print 'Bar',
             elif (i%3 == 0):
                  print 'Foo',
             else:
                  print i,
 
if __name__ == "__main__": out_print()
