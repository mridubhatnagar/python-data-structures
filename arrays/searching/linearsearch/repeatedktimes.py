"""
Problem Statement - https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/repeated-k-times/
"""
'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

def calculate_repeatation(integer_values):
    L=[]
    integer_values.sort()
    unique_values=list(set(integer_values))
    unique_values.sort()
    for number in unique_values:
        count=integer_values.count(number)
        L.append((number, count))
    return L
    
def find_number(L, repeatation_times):
    for value in L:
        if value[1] == repeatation_times:
            key=value[0]
            break
    return key
    
# Write your code here
total_integers=int(input())
integer_values= [int(x) for x in input().split()]
repeatation_times=int(input())

L = calculate_repeatation(integer_values)
num = find_number(L, repeatation_times)
print(num)