# 列表生成式
```python
for color in colors: 
    for size in sizes:
        print((color, size))

tshirts = [(color, size) for size in sizes for color in colors]

# 注意，这里两个循环的嵌套关系和上面列表推导中 for 从句的先后顺序一样
```
# pythonpath
模块路径
系统变量


# command line
# 交互式载入
python -i <file>

# 使用模块
python -m <model_name>

# // 整除符号

# 限制反转
# 这样可能不是高效的,,但是,,思维模型上比较好
n = 137
bin(n)[-1:1:-1]
===
变量作用域（scope）在Python中是一个容易掉坑的地方。 
Python的作用域一共有4中，分别是：

L （Local） 局部作用域
E （Enclosing） 闭包函数外的函数中
G （Global） 全局作用域
B （Built-in） 内建作用域
以 L –> E –> G –>B 的规则查找，即：在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内建中找。

Python除了def/class/lambda 外，其他如: if/elif/else/ try/except for/while并不能改变其作用域。定义在他们之内的变量，外部还是可以访问。
===

# str to list
list & sorted

# chr() & ord()

# all() & any()

# getattr() 通过字符串获取对象..

# exec() & eval()
compile()

# if elif ... else

#int & format
int('00100',2)


```python
s = "0123456789"

# [1,3) like range
s[1:3]Z
```

```python
a = sets[0]
b= sets[0]
a is b
# 注意,不要用,很麻烦

p += 1
# 直接修改了p的引用的内容

p = p + 1
# 改变了p的引用
```