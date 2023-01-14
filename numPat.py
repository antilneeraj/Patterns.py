'''
Author: Neeraj
Date: January 14, 2023

Program to Print following pattern:
Input = 5
1 
6 2 
10 7 3 
13 11 8 4 
15 14 12 9 5
'''

while True:

    try:
        rows = int(input("Input: "))
        nRef=1

        if rows < 0:
            raise ValueError()
        
        for i in range(1, rows + 1):
            nRes = nRef

            for j in range(1,i+1):
                print(nRes, end=' ')
                nRes -= (rows - i + j)
            print()
            nRef += 1 + (rows - i)

    except ValueError:
        print("Invalid Input!, Only Positive Integers are Allowed.")