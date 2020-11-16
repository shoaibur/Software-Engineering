def minimum_bracket_reversal(brackets):
    if len(brackets) % 2: return -1
    open_stack = []
    close_stack = []
    for b in brackets:
        if b in '(':
            open_stack.append(b)
        elif b in ')':
            if open_stack != []:
                open_stack.pop()
            else:
                close_stack.append(b)
    return len(open_stack)//2 + len(close_stack)//2
  
