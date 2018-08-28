```python
from collection import deque
dtest = deque(maxlen=5)
dtest.append(1)
```

更一般的，deque 类可以被用在任何你只需要一个简单队列数据结构的场合。如果
你不设置最大队列大小，那么就会得到一个无限大小队列，你可以在队列的两端执行添
加和弹出元素的操作。
```python
dtest.append()
dtest.pop()

dtest.appendleft()
dtest.popleft()
```