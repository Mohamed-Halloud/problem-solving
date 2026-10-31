class Solution:
    def tribonacci(self, n: int) -> int:
        d = []
        d.append(0)
        d.append(1)
        d.append(1)
        for i in range(3,n+1):
            d.append(d[i-1] + d[i-2] + d[i-3])

        return d[n]