```python
from collections import Counter

tasks = ["A","A","A","B","B","B"]
n = 2

def leastInterval(self, tasks, N):
    task_counts = collections.Counter(tasks).values()
    M = max(task_counts) # 가장 큰 빈도수
    Mct = task_counts.count(M) # 최대 빈도수에 해당하는 태스크의 개수
    return max(len(tasks), (M - 1) * (N + 1) + Mct)
```

