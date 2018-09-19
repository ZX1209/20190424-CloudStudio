# index
defaultdict , deque


# defaultdict 有默认值的字典
```python
s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
d = defaultdict(list)
for k, v in s:
    d[k].append(v)
sorted(d.items())
[('blue', [2, 4]), ('red', [1]), ('yellow', [1, 3])]

# This technique is simpler and faster than an equivalent technique using dict.setdefault():
```




# deque 双端队列
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