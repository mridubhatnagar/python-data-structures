"""
The balanced parentheses problem shown above is a specific case of a 
more general situation that arises in many programming languages. 
The general problem of balancing and nesting different kinds of 
opening and closing symbols occurs frequently. For example, in Python 
square brackets, [ and ], are used for lists; curly braces, { and }, are 
used for dictionaries; and parentheses, ( and ), are used for tuples and arithmetic 
expressions.

Problem Source:

Problem Solving Data Structures and Algorithm using Python Book
Hackerearth - https://www.hackerearth.com/practice/data-structures/stacks/basics-of-stacks/practice-problems/algorithm/balanced-brackets-3-4fc590c6/
"""
from stack import Stack 


def check_parenthesis(s):
    stack_object=Stack()
    balanced=True
    for i in range(0, len(s)):
        if s[i] in ['(', '{', '[']:
            stack_object.push(s[i])
        elif s[i] in [')', '}', ']']:
            if not stack_object.isempty():
                top_element=stack_object.peek()
                if ((s[i] == ']') and (top_element == '[')) or ((s[i] == '}') and (top_element == '{')) or ((s[i] == ')') and (top_element == '(')):
                    stack_object.pop()
            else:
                balanced=False
                break

    if stack_object.isempty() and balanced:
        result='String is balanced'
    else:
        result='String is not balanced'

    return result

"""
Testing 

output = check_parenthesis('{{[[(())]]}}')
print(output)
"""

