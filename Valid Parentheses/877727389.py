class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        counts = {'(': 0, '{': 0, '[':0, ')':0, '}':0, ']':0}

        for char in s:
            counts[char] += 1

            if char == '(':
                stack.append(')')
            elif char == '{':
                stack.append('}')
            elif char == '[':
                stack.append(']')
            else:
                if len(stack) == 0:
                    return False
                if char != stack.pop():
                    return False

        if len(stack) != 0:
            return False

        return True
