class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        s = ""
        n1 = len(word1)
        n2 = len(word2)

        i = 0
        while i < n1 and i < n2:
            s += word1[i]
            s += word2[i]

            i += 1

        s += word2[i:]
        s += word1[i:]

        return s