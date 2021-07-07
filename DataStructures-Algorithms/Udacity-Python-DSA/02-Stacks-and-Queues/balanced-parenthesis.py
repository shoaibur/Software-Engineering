# Equation checker
def is_balanced(equation):
    parenthesis = ''.join([p for p in equation if p in '(){}[]'])
    return is_valid(parenthesis)

def is_valid(parenthesis):
    stack = []
    for p in parenthesis:
        if p in '(':
            stack.append(p)
        elif p in ')':
            if stack == []:
                return False
            stack.pop()
    if stack != []:
        return False
    return True
