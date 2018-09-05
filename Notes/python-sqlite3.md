```python
import sqlite3

connect = sqlite3.connect('database')
cursor = connect.cursor()


cursor.execute()


connect.commit()
connect.close()
```

# 创建表
CREATE TABLE database_name.table_name(
   column1 datatype  PRIMARY KEY(one or more columns),
   column2 datatype,
   column3 datatype,
   .....
   columnN datatype,
);
# 自增主键
ID INTEGER PRIMARY KEY NOT NULL

## 自增插入
insert into QUOTES(QUOTE) values(?)

# 插入
INSERT INTO TABLE_NAME [(column1, column2, column3,...columnN)]  
VALUES (value1, value2, value3,...valueN);



# 查看表列信息
# 比如 表 douban_move
PRAGMA table_info(douban_move)

# 排序语法
SELECT column-list 
FROM table_name 
[WHERE condition] 
[ORDER BY column1, column2, .. columnN] [ASC | DESC];
