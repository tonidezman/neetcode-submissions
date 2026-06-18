mappings = {
    "(": ")",
    "[": "]",
    "{": "}",
}

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for brace in s:
            if brace in mappings:
                stack.append(mappings[brace])
            elif not stack or brace != stack.pop():
                return False
        return len(stack) == 0
        

"""
([{}])
      ^

stack

"""