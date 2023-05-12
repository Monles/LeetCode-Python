# https://leetcode.com/problems/plus-one/
# 1
class Solution:
    def plusOne(self, digits):
        strings = ""
        for number in digits:
            strings += str(number)
        temp = str(int(strings)+1)

        return [int(temp[i]) for i in range(len(temp))]

# 2


class Solution:
    def plusOne(self, digits):
        carry = 0
        n = len(digits)
        for i in reversed(range(n)):
            val = digits[i] + carry + 1 if i == n-1 else digits[i] + carry
            if val <= 9:
                digits[i] = val
                carry = 0
            else:
                carry = val // 10
                val -= 10
                digits[i] = val
        if carry:
            digits.insert(0, carry)
        return digits
