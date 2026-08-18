class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort()

        def backtraking(idx: int, cur: List[int], total: int):
            if total == target:
                res.append(cur.copy())
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i - 1]:
                    continue
                if total + candidates[i] > target:
                    break

                cur.append(candidates[i])
                backtraking(i + 1, cur, total + candidates[i])
                cur.pop()

        backtraking(0, [], 0)
        return res

