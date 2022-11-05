import math
import os
import random
import re
import sys
def r(s,n):
    return (s.count('a')*(n//len(s))+s[:n%len((s))].count('a'))
s=input()
n=int(input())
print(r(s,n))