class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for i in range(len(operations)):
            if operations[i] == "+":
                result.append(int(result[-1]) + int(result[-2]))
            elif operations[i] == "C":
                result.pop()
            elif operations[i] == "D":
                result.append(int(result[-1]) * 2)
            else :
                result.append(int(operations[i]))

        return sum(result)
