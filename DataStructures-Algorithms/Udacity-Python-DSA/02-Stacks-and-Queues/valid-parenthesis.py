def is_valid(parenthesis):
    if parenthesis[0] in ')}]': return False
    if len(parenthesis) % 2: return False
    stack = []
    pairs = {')':'(', '}':'{', ']':'['}
    for p in parenthesis:
        if p in '({[':
            stack.append(p)
        elif p in ')}]':
            if stack == []:
                return False
            check_p = stack.pop()
            if check_p != pairs[p]:
                return False
    if stack != []:
        return False
    return True
  
    
