"""
Problem Statement - https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/min-max-8/
"""




'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

############################################

Solution approach 1
def min_max(total_integers, integer_values):
    L=[]
    for i in range(0, total_integers):
        total=0
        for j in range(0, total_integers):
            if i!=j:
                total = total + int(integer_values[j])
        L.append(total)
    minimum = min(L)
    maximum = max(L)
    
    return minimum, maximum


# Write your code here
total_integers=int(input())
integer_values=input().split()

minimum_num, maximum_num = min_max(total_integers, integer_values)
print(minimum_num, maximum_num)

############################################

Solution approach 2

def min_max(total_integers, integer_values):
    L = [sum(integer_values[:i] + integer_values[i+1:]) for i in range(0, total_integers)]
    minimum=min(L)
    maximum=max(L)
    return minimum, maximum

# Write your code here
total_integers=int(input())
integer_values=list(map(int, input().split()))

minimum_num, maximum_num = min_max(total_integers, integer_values)
print(minimum_num, maximum_num)

#############################################

Solution approach 3 
# Optimized Solution from O(N^2) to O(N)

def min_max(total_integers, integer_values):
    L=[]
    total=sum(integer_values)
    for i in range(0, total_integers):
        result = total - integer_values[i]
        L.append(result)
    minimum=min(L)
    maximum=max(L)
    return minimum, maximum

# Write your code here
total_integers=int(input())
integer_values=list(map(int, input().split()))

minimum_num, maximum_num = min_max(total_integers, integer_values)
print(minimum_num, maximum_num)