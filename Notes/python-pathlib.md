# basic
```py
from pathlib import Path
p = Path('./c')
p.resolve() # 解决符号连接

p / 'c.py'

p.glob(*.py)

...
```


basename = Path(r'D:\储存，安装\14049\Music')



// test ok...

fullname = =basename /  '\"Lana Del Rey - Love.mp3\"'



os and os.path  pathlib
os.path.abspath()   Path.resolve()
os.chmod()  Path.chmod()
os.mkdir()  Path.mkdir()
os.rename() Path.rename()
os.replace()    Path.replace()
os.rmdir()  Path.rmdir()
os.remove(), os.unlink()    Path.unlink()
os.getcwd() Path.cwd()
os.path.exists()    Path.exists()
os.path.expanduser()    Path.expanduser() and Path.home()
os.path.isdir() Path.is_dir()
os.path.isfile()    Path.is_file()
os.path.islink()    Path.is_symlink()
os.stat()   Path.stat(), Path.owner(), Path.group()
os.path.isabs() PurePath.is_absolute()
os.path.join()  PurePath.joinpath()
os.path.basename()  PurePath.name
os.path.dirname()   PurePath.parent
os.path.samefile()  Path.samefile()
os.path.splitext()  PurePath.suffix