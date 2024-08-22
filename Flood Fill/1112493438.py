class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        q = []
        q.append((sr, sc))
        visited = set() 
        toReplace = image[sr][sc]
        m = len(image)
        n = len(image[0])

        while q:
            toAdd = []

            for _ in range(len(q)):
                cur = q.pop()
                visited.add(cur)
                image[cur[0]][cur[1]] = color

                for i in [1, -1]:
                    if (cur[0] + i) < 0 or (cur[0] + i) >= m:
                        continue

                    if (cur[0] + i, cur[1]) in visited:
                        continue

                    if image[cur[0] + i][cur[1]] == toReplace:
                        toAdd.append((cur[0] + i, cur[1]))

                for j in [1, -1]:
                    if (cur[1] + j) < 0 or (cur[1] + j) >= n:
                        continue

                    if (cur[0], cur[1] + j) in visited:
                        continue

                    if image[cur[0]][cur[1] + j] == toReplace:
                        toAdd.append((cur[0], cur[1] + j))
                
            q.extend(toAdd)

        return image


# 0, 0
# 0, 1
# 1, 0
# 1, 1

# 0, 1
# 0, -1
# 1, 0
# -1, 0
                



