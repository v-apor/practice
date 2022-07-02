# Approach 1: Keep pushing in stack for each of opening bracket & when closing bracket comes up, pop and check if it's correct
# Return false if the stack isn't empty after traversal or if closing bracket is encountered when stack is empty
# Time O(n) | space O(n)

def isValid(s):
    brack_stack = []
    brack_pairs = {'(':')', '[':']', '{':'}'}
    for brack in s:
        if brack in ['(', '[', '{']:
            brack_stack.append(brack)
        else:
            if len(brack_stack) == 0:
                return False
            last = brack_stack.pop()
            if brack != brack_pairs[last]:
                return False
    return True if len(brack_stack) == 0 else False

print(isValid("]"))