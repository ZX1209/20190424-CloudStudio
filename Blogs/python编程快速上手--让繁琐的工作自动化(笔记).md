[TOC]





# python编程快速上手--让繁琐的工作自动化(笔记)

> 自用,当作笔记提个醒,,
>
> 顺便推荐下这本书书..
>
> > 动手试试才能更好的掌握

---



## 前言

> 如何寻求帮助
>
> * `help()` 
> * `dir()`
>
> 网站
>
> - [Google](https://google.com)
>
> - [StackOverFlow](https://stackoverflow.com/)
>
> - [reddit-learnprogramming](https://www.reddit.com/r/learnprogramming/)
>
>   



> 聪明的提出编程问题
>
> > * 说明你打算做什么,而不是你做了什么
> > * 明确指出发生错误的地方.(它是在程序每次启动时发生,还是在你做了某些动物之后?)
> > * [pastebin](https://pastebin.com/) and [gist](https://gist.github.com/) 与他人共享大量代码,而不丢失格式
> > * 解释你为了解决这个问题已经尝试了那些方法.这会告诉别人你已经做了一些工作来搞清楚情况
> > * 列出啊你使用的python版本(嗯,环境...)
> > * 如果错误在你更改了代码之后出项,准确说明你该了什么
> > * 说明如何重现错误
> > * 遵守良好的在线礼节,例如,不要全用大写提问,或者试图对帮助年纪的人提出无礼的要求
> > * [作者博客](http://inventwithpython.com/blog) 与 邮件(al@inventwithpython.com)
> > * 



## 第一部分 python 基础



### 第一章 Python 基础

交互式环境

`整数`  `浮点数`  `字符串`(连接:`+`   复制:`*`)



> 变量名
>
> 1. 只能是一个词(中文,只要是unicode都行)
> 2. 只能包含字母,数字和下划线..
> 3. 不能以数字开头



`print()`

`inpout()`

`len()`

`str()` `int()` `float()`

`#` `''' '''` 注释



### 第二章 控制流

布尔值: `True` `Flase`

比较操作符: `==` `!=` `<`  `>` `<=` `>=`

布尔操作符: `and` `or` `not`



控制流

```python
# if
if name=='Alice':
  print('Hi, Alice')
  
  
# else
if name == 'Alice':
  print('Hi, Alice')
else:
  print('who are you')
  
# elif
if name =='Alice':
  print('Hi, Alice')
elif age < 12:
  print('you are not Alice')
  
  
# if what: elif what: else:
if name =='Alice':
  print('Hi, Alice')
elif age < 12:
  print('you are not Alice')
else:
  print('who are you')

```



`while`

`break` `continue`



`for i in range(10): ...`

`import`  `from ... import .. as ...`

`sys.exit()`

### 第三章 函数

`def `

`return`

`None`  没有返回值的函数还是会返回None

'关键字参数' : `print("this",end='')`

```python
try:
  code
except errortype :
  error handle
```



`global` : 使用全局变量..

### 第四章 列表

```python
# 创建 and 初始化 list
a_list = []
another_list = [1,"2"]

# (正|负)下标
# 切片
# for i in list:

```

`in`   `not in`



`index()` : 传入值 ,返回 下标
`append()`  `insert()` `remove()`

`sort() `

列表可以跨多行...



字符串与元组都是不可变的



`list()`  `tuple()`



变量的==引用==关系

`copy.copy()`  `copy.deepcopy()`

 

多重赋值

### 第五章 字典和结构化数据

```python
myCats = {'size':'fat','color':'gray','disposition':'loud'}

myCats['size'] 
# fat
```

`.key()`  `.values()`  `.items()`

`.get()`  `.setdefault()`

`pprint.pprint()`

`pprint.pformat()`

### 第六章 字符串操作



##  第二部分 自动化任务

### 第七章 模式匹配与正则表达式

`re`


### 第八章 读写文件

### 第九章 组织文件

### 第十章 调试

### 第十一章 从Web抓取信息

`webbrowser` 模块(用默认游览器打开连接)\

`pyperclip`模块 (系统剪切板调用)

`requests` 模块

`bs4`模块(beautifulSoup4 解析提取网页内容)

`selenium`模块 可直接控制的游览器

###第十二章 处理Excel 电子表格

`openpyxl`模块

### 第十三章 处理 PDF 和 Word 文档

`pyPDF2`

`python-docx`

### 第十四章 处理CSV文件和JSON数据

`csv`
`json`

### 第十五章 保持任务,计划任务和启动程序

`time`
`datetime`

`threading`

`subprocess`

### 第十六章 发送电子邮件和短信

`smtplib`

`imaplib`  `imapclient`



`twilio`

### 第十七章 操作图像

`Plilow`

`PIL`

### 第十八章 用GUI自动化控制键盘和鼠标

#### h4

##### h5





 `pyauotgui`

