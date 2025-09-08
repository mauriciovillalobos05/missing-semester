class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        a = b = carry = 0
        digit_idx = 1
        while n > 0:
            digit = n % 10
            n //= 10

            target = digit - carry
            if target < 2:
                if n == 0:
                    a += digit_idx * target
                else:
                    carry = 1
                    a += digit_idx * (1 if target == -1 else 1 + target)
                    b += digit_idx * (8 if target == -1 else 9)
            else:
                carry = 0
                a += digit_idx * 1
                b += digit_idx * (target - 1)

            digit_idx *= 10

        return [a, b]
