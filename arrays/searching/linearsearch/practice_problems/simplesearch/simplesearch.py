"""
Problem Statement - https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/simple-search-4/
"""

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

# Write your code here

total_integers=int(input())
numbers=input()
L = numbers.split()
search_element=int(input())
    
for element in enumerate(L):
    if int(element[1])==int(search_element):
        result = element[0]
        break
    else:
        result = -1
print(result)
    
