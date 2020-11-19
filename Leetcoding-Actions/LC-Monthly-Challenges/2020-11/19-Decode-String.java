class Solution {
    public String decodeString(String s) {
        Stack<Character> stack = new Stack<>();
        int i = 0;
        while (i < s.length()) {
            if (s.charAt(i) != ']') {
                stack.push(s.charAt(i));
            } else {
                List<Character> charList = new ArrayList<>();
                while (!stack.isEmpty()) {
                    char ch = stack.pop();
                    if (ch == '[') {
                        break;
                    } else {
                        charList.add(ch);
                    }
                }
                int base = 1;
                int k = 0;
                while (!stack.isEmpty()) {
                    if (Character.isDigit(stack.peek())) {
                        k = k + (stack.pop() - '0') * base;
                        base *= 10;
                    } else {
                        break;
                    }
                }
                while (k != 0) {
                    for (int j = charList.size() - 1; j >= 0; j--) {
                        stack.push(charList.get(j));
                    }
                    k--;
                }
            }
            i++;
        }
        char[] result = new char[stack.size()];
        for (int k = result.length - 1; k >= 0; k--) {
            result[k] = stack.pop();
        }
        return new String(result);
    }
}
