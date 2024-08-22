class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree = {}
        adjacent = defaultdict(list)
        queue = deque()
        order = []

        # setting adjacency and in-degree maps
        for i in range(numCourses):
            degree[i] = 0

        for req in prerequisites:
            degree[req[0]] += 1
            adjacent[req[1]].append(req[0])

        # adding all 0 in-degree courses to queue
        for course in degree:
            print(degree[course])
            if degree[course] == 0:
                queue.append(course)
        
        print(queue)
        
        while queue:
            val = queue.popleft()
            order.append(val)

            if val in adjacent:
                for course in adjacent[val]:
                    degree[course] -= 1
                    if degree[course] == 0:
                        queue.append(course)
                
        if len(order) == numCourses:
            return order
        
        return []

        
