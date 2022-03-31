class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict1 = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }
        output = []

        def dfs(index, path):
            if len(path)==len(digits):
                output.append(path)
                return
            for i in range(index, len(digits)):
                try:
                    for j in dict1[digits[i]]:
                        dfs(i+1, path+j)
                except KeyError:
                    return []

        dfs(0, "")
        if not digits:
            return []
        return output