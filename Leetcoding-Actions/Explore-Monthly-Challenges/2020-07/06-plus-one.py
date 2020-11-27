def plusOne(digits):
    carry = 1
    for i in range(len(digits)-1, -1, -1):
        summ = digits[i] + carry
        carry, s = divmod(summ, 10)
        digits[i] = s
        if carry == 0:
            return digits
    if carry:
        return [1] + digits
