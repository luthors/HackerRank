import math
import os
import random
import re
import sys
def multi_delete(list_, args):
    indexes = sorted(args, reverse=True)
    for index in indexes:
        del list_[index]
    return list_
def makeAnagram(a, b):
    # Write your code here
    c=list(a)
    d=list(b)
    c.sort()
    d.sort()
    temp=0
    indices=[]
    for i in range(len(c)):
        if not (c[i] in d):
            indices.append(i)
            temp+=1
    multi_delete(c, indices)
    indices=[]
    for i in range(len(d)):
        if not (d[i] in c):
            indices.append(i)
            temp+=1
…   return temp
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
