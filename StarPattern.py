"""
First take a random Range from user. This range is the amount of stars will appear in last line
If user inputs a Even number, minus one to get the Closest Odd number
Running through a For loop of range from 1 to The range which user inputed, and the step is two for getting only the odd numbers

Make stars of the amount of the loop Number.
And for getting the space amount, the algorithm is:
    userRange - the number of loop and devide by 2
Explanation:
    Suppose the range is 5, the first line will have 2 Spaces, then a Star. So the amount of spaces are the half of the number of the Difference between range and the loop number, whice is (in this case) 2.
    So, 2 spaces (  ) + The number of loop amount Star (1x* = *) = "  *"

"""



_range = int(input("Enter Range:> "))
if (_range%2 == 0):
    _range -= 1
print("")

for i in range(1, _range, 2):
    star = "*"*i
    space = " " * int((_range-i)/2)
    print(space+star)
