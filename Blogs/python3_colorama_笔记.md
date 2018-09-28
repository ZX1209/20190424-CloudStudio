# python3 colorama 笔记

## 基本使用

### 初始化

```python
from colorama import init
init()
```

> 初始化基本上针对window 平台,但为了保持兼容性还是先初始化一下的好

### 常用

```python
from colorama import init , Fore, Back,Style
print(Fore.RED + "这是一段前景为红色的文本") # foreground 前景
```

## 参考

```python
import colorama 
dir(colorama)
dir(colorama.Fore)
# ...

```

