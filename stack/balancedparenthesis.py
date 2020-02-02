"""
Balanced Parenthesis uses the concept of stack.

Balanced parentheses means that each opening symbol 
has a corresponding closing symbol and the pairs of parentheses are properly nested.

In the below solution only round brackets are considered in the given string.

"""
from stack import Stack

def check_parenthesis(s):
    stack_object = Stack()
    balanced = True
    for i in range(0, len(s)):
        if s[i] == '(':
            stack_object.push(s[i])
        elif s[i] == ')':
            if stack_object.size() > 0:
                stack_object.pop()
            else:
                balanced = False
                break
    if stack_object.isempty() and balanced:
        result='String is balanced'
    else:
        result='String is unbalanced'
    return result

"""
Testing

c = check_parenthesis('(()))')
print(c)

"""