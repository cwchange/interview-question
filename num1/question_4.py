"""
4. Given: words = [‘one’, ‘one’, ‘two’, ‘three’, ‘three’, ‘two’] Remove the duplicates.
"""



#Solution number one, by using numpy build in function.
import numpy as np
 
words = ['one', 'one', 'two', 'three', 'three', 'two']
 
new_words=np.unique(np.array(words))
print new_words


#soltion number two
class q_4:
        def __init__(self, array):
               self.array=array
               self.final=[]
 
        def insert(self):
              for i in self.array:
                    if i not in self.final:
                         self.final.append(i)
 
if __name__ == "__main__":
    words=['one', 'one', 'two', 'three', 'three', 'two']
    temp=q_4(words)
    temp.insert()
    print temp.final
