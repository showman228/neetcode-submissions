class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = set()
        candidates.sort()

        def dfs(i: int, cur: List[int], total: int):
            if total == target:
                res.add(tuple(cur))
                return

            if total > target or i == len(candidates):
                return

            cur.append(candidates[i])
            dfs(i + 1, cur, total + candidates[i])
            cur.pop()

            dfs(i + 1, cur, total)

        dfs(0, [], 0)
        return [list(comb) for comb in res]
        