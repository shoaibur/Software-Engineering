class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        i = 0
        while i < len(s):
            if s[i] != ']':
                stack.append(s[i])
            else:
                string = ""
                while stack:
                    char = stack.pop()
                    if char == '[': break
                    string += char
                k = ""
                while stack:
                    if stack[-1].isdigit():
                        k += stack.pop()
                    else: break
                k = int(k[::-1])
                string = k * string[::-1]
                for char in string:
                    stack.append(char)
            i += 1
        return ''.join(stack)
