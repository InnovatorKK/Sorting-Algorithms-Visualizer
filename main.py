import random
from tkinter import *
import time
import os
import sort.bubble, sort.insert, sort.selection


def Log(arr, comparing):
    line = ["  " for i in range(16)]
    for i in range(15, -1, -1):
        idx = arr.index(i)
        if idx == comparing[0] or idx == comparing[1]:
            line[idx] = "🟥"
            
        else:
            line[idx] = "⬛"
        print(line)



if __name__ == "__main__":
    
    SORTTYPE = input()
    #SORTTYPE = "SELECTION"
    sleep = 0.05
    arr = random.sample(range(0, 16), 16)



    if SORTTYPE == "BUBBLE":
        result = sort.bubble.Bubble(arr)
        i_ = -1
        for i in result[0]:
            i_ += 1
            os.system('clear')
            Log(i, result[3][i_]) #reusult[3] == comparing
            time.sleep(sleep)
        print("Bubble Sort")
        print(f"Compairs: {result[2]}\nSwaps: {result[1]}")
        print("\033[38;2;215;95;215m" + "TASK FINISED SUCCESFULLY" + "\033[0m")
    
    if SORTTYPE == "INSERT":
        i_ = -1
        result_insert = sort.insert.Insert(arr)
        for i in result_insert[0]:
            i_ += 1
            os.system('clear')
            Log(i, result_insert[3][i_]) #reusult[3] == comparing
            time.sleep(sleep)
        print("Insert Sort")
        print(f"Compairs: {result_insert[2]}\nSwaps: {result_insert[1]}")
        print("\033[38;2;215;95;215m" + "TASK FINISED SUCCESFULLY" + "\033[0m")
        
    if SORTTYPE == "SELECTION":
        i_ = -1
        result_selection = sort.selection.Selection(arr)
        for i in result_selection[0]:
            i_ += 1
            os.system('clear')
            Log(i, result_selection[3][i_]) #reusult[3] == comparing
            time.sleep(sleep)
        print("Selection Sort")
        print(f"Compairs: {result_selection[2]}\nSwaps: {result_selection[1]}")
        print("\033[38;2;215;95;215m" + "TASK FINISED SUCCESFULLY" + "\033[0m")
