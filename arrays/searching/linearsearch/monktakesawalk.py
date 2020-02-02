"""
Problem Statement - https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/monk-takes-a-walk/
"""

def count_vowels(string):
    count=0
    vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    for letter in string:
        if letter in vowels:
            count+=1
    return count



# Write your code here
test_cases = int(input())
all_inputs = []
for i in range(test_cases):
    value=input()
    count=count_vowels(value)
    print(count)
