class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        return "".join(str(len(s))+ "#" + s  for s in strs)
            
    def decode(self, s: str) -> List[str]:
        if s == "#":
            return []
        else :
            result = []
            i = 0
            while i < len(s):
                j = i

                while s[j] != "#":
                    j += 1

                lenght = int(s[i:j])

                start = j + 1
                end = start + lenght

                result.append(s[start:end])

                i = end

            return result
        
