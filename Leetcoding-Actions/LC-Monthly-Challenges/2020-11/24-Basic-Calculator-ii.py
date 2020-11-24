class Solution:
    def calculate(self, s: str) -> int:
        prevOperator = "+"
        
        num = 0
        result = 0
        temp = 0
        
        for char in s+"+":
            if char.isdigit():
                num = num * 10 + int(char)
            elif char in "+-*/":
                currOperator = char
                if prevOperator == "+":
                    result += temp
                    temp = num
                elif prevOperator == "-":
                    result += temp
                    temp = -num
                elif prevOperator == "*":
                    temp *= num
                else:
                    temp = int(temp / num)
                num = 0
                prevOperator = currOperator
        
        return result + temp
