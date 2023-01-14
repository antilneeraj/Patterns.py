'''
To Print the following Alpha Pattern:
5
     A
    ABA
   ABCBA
  ABCDCBA
 ABCDEDCBA
Author: Neeraj
Date: December 16, 2022
'''

sampleW = ''
flag = 0 
row = int(input())
space = row

for i in range (1, row+1):
  n = 65
  for k in range(space):
    print(" ", end="")

  for alpha in range(i):
    print(chr(n), end="")
    if flag == 1:
      sampleW += chr(n)
    n = n+1

  space -= 1
  if flag==1:
    sampleW = sampleW[:-1]
    print(sampleW[::-1], end="")
  print()
  flag = 1
  sampleW = ''