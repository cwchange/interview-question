"""
2. Write a function that counts the number of even numbers that appear in a range of integers 0..n, where n is supplied as the sole argument to your function. Example: even_integers(3) 1
"""


#Solution to question 2
def even_integers(n):
        temp=0
        for i in xrange(n+1):
              if ((i != 0) and (i%2 == 0)):
                     temp+=1
        print temp

 
if __name__ == "__main__": even_integers(10)
