"""
Problem Solving - https://www.hackerearth.com/practice/algorithms/searching/linear-search/practice-problems/algorithm/breakup-app/
"""
import re

# Write your code here
g_count, m_count=0,0
message_count=int(input())
for i in range(0, message_count):
    string=input()
    dates=re.findall(r'[0-9]+', string)
    for date in dates:
        if int(date) in [19, 20]:
            g_count=(g_count+2) if string[0]=="G" else (g_count+1)
        else:
            m_count=(m_count+2) if string[0]=="G" else (m_count+1)

if g_count>m_count:
    print("Date")
else:
    print("No Date")