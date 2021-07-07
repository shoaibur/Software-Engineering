class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        if not tasks: return 0
        if n == 0: return len(tasks)
        
        counter = collections.Counter
        taskCounter = counter(tasks)
        taskCounter = sorted(taskCounter.items(), key = lambda x: x[1], reverse=True)
        
        taskMax = taskCounter[0][1]
        idleTime = (taskMax - 1) * n
        
        for i in range(1, len(taskCounter)):
            idleTime -= min(taskMax-1, taskCounter[i][1])
        idleTime = max(idleTime, 0)
        
        return len(tasks) + idleTime
        
