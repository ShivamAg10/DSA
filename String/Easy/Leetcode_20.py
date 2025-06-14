class Solution:
    def isValid(self, s: str) -> bool:
        s_dict = {
            ')' : '(',
            '}' : '{',
            ']' : '['
        }

        stack = []

        for b in s:
            if b in s_dict:
                if s_dict[b] not in stack:
                    return False
                top_element = stack.pop()
                if s_dict[b] != top_element:
                    return False
            else:
                stack.append(b)
        return not stack