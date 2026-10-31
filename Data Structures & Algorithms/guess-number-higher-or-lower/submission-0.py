class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            k = left + (right - left) // 2

            result = guess(k)

            if result == 0:
                return k

            elif result == -1:
                right = k - 1

            else:
                left = k + 1