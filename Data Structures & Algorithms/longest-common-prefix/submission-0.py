class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        out = strs[0]
        while out:
            if all(s.startswith(out) for s in strs):
                return out
            out = out[:-1]
        

        return ""
            