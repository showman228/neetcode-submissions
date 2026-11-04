class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Есть ли цикл в графе? да -> false, нет -> true
        preHash = [[] for i in range(numCourses)]

        for i, pre in prerequisites:
            preHash[pre].append(i)
        
        state = [0] * numCourses # 0 -> не посещали 1 - обрабатываем 2 - обработали

        def dfs(node: int):
            if state[node] == 1:
                return True
            if state[node] == 2:
                return False

            state[node] = 1
            for nei in preHash[node]:
                if dfs(nei):
                    return True
            state[node] = 2
            return False
        
        for i in range(numCourses):
            if dfs(i): return False
        return True