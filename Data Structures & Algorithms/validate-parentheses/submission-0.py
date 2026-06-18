class Solution:
    def isValid(self, s: str) -> bool:
        mapping = {
            "(": ")",
            "[": "]",
            "{": "}",
        }
        stack = []
        for brace in s:
            if brace in mapping:
                stack.append(mapping[brace])
            else:
                if len(stack) == 0 or stack.pop() != brace:
                    return False
        return len(stack) == 0
