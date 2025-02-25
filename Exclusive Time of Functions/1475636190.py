class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        times = defaultdict(int)
        callStack = []

        for log in logs:
            curFunc, curAction, t = log.split(":")
            curTime = int(t) 

            if not callStack:
                callStack.append((curFunc, curAction, curTime))
                continue
            else:

                lastFunc, lastAction, lastTime = callStack[-1]

                if curAction == "start":
                    times[lastFunc] += curTime - lastTime
                    callStack.append((curFunc, curAction, curTime))
                else: 
                    times[lastFunc] += curTime - lastTime + 1
                    callStack.pop()

                    if callStack:
                        callStack[-1] = (callStack[-1][0], callStack[-1][0], curTime + 1)


        
        ret = [0] * len(times)

        for func in times:
            ret[int(func)] = times[func]
        
        return ret