# 4 10 5 / * --> 4 * (10 / 5) = 8
# 12 4 10 5 / * - 3 + --> 12 - 4 * (10 / 5) + 3 = 7
# Algorithm
# for each item
    # if number: push it to stack
    # if operation: (i) pop two numbers (ii) apply operation (iii) push the result to the stack

def reverse_polish_notation(s):
    stack = []
    for item in s:
        if item in '+-*/':
            second = stack.pop()
            first = stack.pop()
            if item == '+':
                result = first + second
            elif item == '-':
                result = first - second
            elif item == '*':
                result = first * second
            elif item == '/':
                result = first // second # considering only integer division
            stack.push(result)
        else:
            stack.push(int(item))
    return stack[0]
