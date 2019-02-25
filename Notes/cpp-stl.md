## 2.1 栈(Stack)

### 导入使用
```cpp
# include <stack>

stack<TYPE> StackName


```

### 成员函数
bool empty()
void pop()
void push(const TYPE &val)
TYPE &top()
size_type size()

### 示例
```cpp
stack<int> s;
s.push(1);
s.push(2);
s.push(3);

cout<<"Top: "<<s.top()<<endl;
cout<<"Size: "<<s.size()<<endl;
s.pop();
cout<<"Size: "<<s.size()<<endl;

if(s.empty()) cout<<"Is empyt"<<endl;
else cout<<"Is not empty"<<endl;

```

## 2.2 向量(Vector)

### 导入使用
```cpp
# include <vector>


```
| 成员函数 | 功能 |
| - | - |
vector<TYPE> c | 产生一个空的Vector,其中没有任何元素
vector<TYPE> c1(c2) | 产生另一个同型Vector的副本(所有元素都被复制)
vector<TYPE> c(n) | 利用元素的Default构造函数生成一个大小为 n  的Vector
vector<TYPE> c(n,leem) | 产生一个大小为 n 的Vector,每个元素都是 elem
`c.~vector<TYPE>()` | 销毁所有元素,并释放内存



### 主要成员函数
| 函数 | 功能 |
| - | - |
c.pop_back() | 删除最后一个数据
c.push_back(elem) | 在尾部加入一个数据 elem
c.empyt() | 判断容器是否为空
c.clear() | 移除容器中所有数据
c.insert(pos,elem) | 在pos位置插入一个elem的副本,传回新数据的位置
c.insert(pos,n,elem) | 在pos位置插入n个elem数据.无返回值
c.insert(pos,beg,end) | 在 pos 位置插入在[beg,end)区间内的数据,无返回值 (另一个数组的区间吧)
c.erase(pos) | 删除pos位置的数据,传回下一个数据的位置
c.erase(beg,end) | 删除在[beg,end)区间内的数据,传回下一个数据的位置
c.size() | 返回容器中实际数据的个数
c.capacity() | 返回已经分配的可以容纳的元素个数
c.begin() | 传回迭代器中的第一个数据地址
c.end() | 传回迭代器中的最后一个数据地址
c.back() | 传回最后一个数据,补减产这个数据是否存在?
c.assign(beg,end) | 将[beg,end)区间内的数据复制并赋值给c
c.assign(n,elem) | 将n个elem的值复制并赋值给c
c1.swap(c2) | 将 c1 和 c2 元素互换
swap(c1,c2) | 将 c1 和 c2 元素互换


### 示例
```cpp
int n;
cin>>n;
vector<int> a(n);
for (int i = 0; i < n; ++i)
{
    cin>>a[i];
}
a.push_back(10)


for (int i = 0; i < n; ++i)
{
    cout<<a[i]<<" ";
}
cout<<a.size()<<endl;

# 迭代器
vector<int>::iterator p;
for(p=a.begin();p!=a.end();++p)
    cout<<*p<<" ";
cout<<endl;

```

## 2.3 映射(Map)

### 导入使用
```cpp
# include <map>

```
成员函数 | 功能
- | -
map c |
map c(op) |
map c1(c2)
map c(beg,end)
map c(beg,end,op)
`c.~map()`

### 成员函数
bool empty()
void pop()
void push(const TYPE &val)
TYPE &top()
size_type size()

### 示例
```cpp
stack<int> s;
s.push(1);
s.push(2);
s.push(3);

cout<<"Top: "<<s.top()<<endl;
cout<<"Size: "<<s.size()<<endl;
s.pop();
cout<<"Size: "<<s.size()<<endl;

if(s.empty()) cout<<"Is empyt"<<endl;
else cout<<"Is not empty"<<endl;



## 2.1 栈(Stack)

### 导入使用
```cpp
# include <stack>

stack<TYPE> StackName


```

### 成员函数
bool empty()
void pop()
void push(const TYPE &val)
TYPE &top()
size_type size()

### 示例
```cpp
stack<int> s;
s.push(1);
s.push(2);
s.push(3);

cout<<"Top: "<<s.top()<<endl;
cout<<"Size: "<<s.size()<<endl;
s.pop();
cout<<"Size: "<<s.size()<<endl;

if(s.empty()) cout<<"Is empyt"<<endl;
else cout<<"Is not empty"<<endl;
```

## 2.1 栈(Stack)

### 导入使用
```cpp
# include <stack>

stack<TYPE> StackName


```

### 成员函数
bool empty()
void pop()
void push(const TYPE &val)
TYPE &top()
size_type size()

### 示例
```cpp
stack<int> s;
s.push(1);
s.push(2);
s.push(3);

cout<<"Top: "<<s.top()<<endl;
cout<<"Size: "<<s.size()<<endl;
s.pop();
cout<<"Size: "<<s.size()<<endl;

if(s.empty()) cout<<"Is empyt"<<endl;
else cout<<"Is not empty"<<endl;
```

# contianer

vector

map?

set?

sort?

make_pair & pair


# algorithm

sort

find

..

# iterator?
