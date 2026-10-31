class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        n1 = len(word1)
        n2 = len(word2)

        for i in range(min(n1, n2)):
            s += word1[i]
            s += word2[i]

        if n1 < n2:
            s += word2[n1:]
        elif n1 > n2 :
            s += word1[n2:]

        return s