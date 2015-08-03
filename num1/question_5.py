"""
5. Print to stdout the following output using only one loop:

1 1 1 1 1

2 2 2 2 2

3 3 3 3 3

4 4 4 4 4

5 5 5 5 5

"""

def out_print(n,m):
       for i in range(1,n+1):
              print '%s ' %(i) *m
   
if __name__ == "__main__": out_print(5,5)
