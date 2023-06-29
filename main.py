import random
from tkinter import *

def Log(arr):
    line = [" " for i in range(16)]
    for i in range(15, -1, -1):
        line[arr.index(i)] = "█"
        print(line)

        
        


arr = random.sample(range(0, 16), 16)

#print(arr)
Log(arr)


