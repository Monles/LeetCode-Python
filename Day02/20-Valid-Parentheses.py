# https://leetcode.com/problems/valid-parentheses/description/
class Solution:

    def isValid(self, s: str) -> bool:
        p_stack = []
        opcl = dict(('()', '[]', '{}'))
        for i in s:
            if i in '([{':
                p_stack.append(i)
            elif len(p_stack) == 0 or i != opcl[p_stack.pop()]:
                return False

        return len(p_stack) == 0
