"""
Problem Statement - https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/special-shop-69904c91/
"""

'''
# Sample code to perform I/O:

name = input()                  # Reading input from STDIN
print('Hi, %s.' % name)         # Writing output to STDOUT

# Warning: Printing unwanted or ill-formatted data to output will cause the test cases to fail
'''

def optimal_cost(all_inputs):
    final_costs=[]
    for cases in all_inputs:
        possible_costs=[]
        N, A, B=cases[0], cases[1], cases[2]
        for i in range(0,N+1):
            cost=A*i**2 + B*(N-i)**2
            possible_costs.append(cost)
        optimal_cost=min(possible_costs)
        final_costs.append(optimal_cost)
    
    for cost in final_costs:
        print(cost)

# Write your code here
total_test_cases=int(input())
all_inputs=[]
for value in range(total_test_cases):
    user_input=[int(x) for x in input().split()]
    all_inputs.append(user_input)
optimal_cost(all_inputs)

