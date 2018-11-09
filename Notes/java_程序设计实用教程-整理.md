# 第一章 java概述
package 声明类所在包
lang 包默认导入
final 常量


# 第二章 java语言基础

## 标识符
以字母开头的字母数字序列
0~9,大小写字母,下划线(_)和符号$

## 注释
// 单行注释

/* 多行注释
*/

/** 文档注释
*/
## 基本数据类型
整数类型    字节数
byte 1
short 2
int 4
long 8
float 4
double 8

> 空语句?
> i = 1;;

## 数组
type[] name
name = new type[10]

type[] name  ={values}

> ArrayList

类的封装包含两层含义:
第一,将数据和对数据的操作包装成一个对象类型,使对象成为包含一组属性和操作的运行单位
第二,实现信息隐藏,类既要提供与外部联系的方法,又要尽可能地隐藏类中某些数据和实现细节,以约束外部的可见性

析构方法
public void finalize()

public static void main(String args[])

## 类的继承性
extends

## 类的多态
父实例(引用指针)(容器)能兼容子实例

在子类的实例成员方法中,可用super引用访问被子类隐藏的父类同名成员变量

沿着继承关系逐层向上

父类对象只能执行那些在父类中声明,被子类覆盖的子类方法,不能执行子类增加的成员方法

## 类的抽象性
public abstract class ColsedFigure
{
    public abstract double area();
}
> 构造方法,静态成员方法不能被声明为抽象方法
> 抽象类通常包含抽象方法,也可以不包含抽象方法,但是包含抽象方法的类必须被声明为抽象类


### 最终类
public final class Math extends Object


# 第三章 类的封装,继承和多态

## 3.2 类的封装性
类的封装包含两层含义,
第一,将数据和对数据的操作包装成一个对象类型,使对象成为包含一组属性和操作的运行单位
第二,实现信息隐藏,类既要提供与外部联系的方法,又要尽可能地隐藏类中某些数据和实现细节.

> 缺省权限 到当前包


### 3.3.2 继承原则及作用


### 3.5.2 抽象类
public abstract class ClosedFigure{
    public abstract double area();
}


# 第四章 接口,内部类和javaa pi基础

## 4.1 接口与实现接口的类
public interface Area{
    public abstract double area();
}

用 implements 声明一个类指定接口
一个类可以实现多个接口,多个接口之间用逗号隔开.

接口与抽象类的区别
抽象类为子类约定声明,抽象类可以给出部分实现包括构造方法等;抽象方法在多个子类中表象出多态性
类的单继承,是的一个类只能继承一个父类的约定和实现

接口为多个互不相关的类约定某一特性的方法声明,在类型层次中表达对象拥有的属性,接口没有实现部分
接口是多继承的.一个类实现多个接口,就具有多种特性,也是多继承的.

一个非抽象类如果声明多个接口,则必须实现(覆盖)所有指定接口中的所有抽象方法,
方法的参数列表必须相同;否则它必须声明为抽象类

## 4.2 内部类和内部接口
是声明在其他类或接口内部的内嵌类型. 
> Pixel$Color.class 和 Pixel$ColorConstant.class

## 4.3 java api基础

### 4.3.1 java.lan 包中的基础类库

#### 1 object 类
string toString()
boolean queals(Object obj)
void finalize() throws Throable
final Class<?> getClass()

#### 2 Math 数学类
final double E
final double PI
static double abs(double a)
static double random()
static double pow(double a,double b)
static double sqrt(double a)
static double sin(double a)

最终类

#### 3 Comparable 可比较接口
public interfacce Comparable<T>{
    public abstract int compareTo(T cobj);
}

#### 4 基本数据类型的包装类
java 为每种基本数据类型声明了一个对应的类,称为基本数据类型的包装类.
Byte,Short,Integer,Long,Float,Doble,Character,Boolean
都是最终类?

##### Integer 最终类
parseInt() -> int i = Integer.parseInt("123");
intValue() -> int j = new Integer("123").intValue();

##### Double 浮点类 最终类
parseDouble(String s) throws NumberFormatException

##### Stirng 字符串类
isEmpty()
toUpperCase()
toLowerCase()
startsWith()
endsWith()
indexOf(int ch)
indexOf(String s)
lastIndexOf()
String[] split(String regex)

trim() 返回当前串删除所有空格后的字符串

##### StringBuffer 字符串缓冲区类


##### 7 Class 和 Package 类
public final class Class<T> implements java.io.Serializable,...{
    public String getName()
    public Class<? super T> getSuperclass()
    public Package getPackage()

}

public class Package extends Object ...{
    public String getName();
}

##### 8 System 系统类
public final class System extends Object{
    ...
    getProperties()
    getProperty()
    currentTimeMillis()
    exit(int status)
    in,out,err
}

##### 9 Runtime 运行时类
public class Runtime extends Object{
    public static Runtime getRuntime()
    public long totalMemory()
    public long freeMemory()
}

### 4.3.2 java.util 包中的工具类库
#### 1 日期类
##### Data 类
public Date();//构造方法,获得系统当前日期时间

##### Calendar 类
Calendar 时抽象类,调用getInstance() 方法创建一个子类实例后,在调用get() 方法通过常量参数获得或时间的指定部分
YEAR,MONTH,DATE,HOUR,MINUTE,SECOND,DAY_OF_WEEK

#### 2. Comparator 比较器接口
equals
compare

#### 3. Arrays 数组类
Arrays 类的所有方法都是静态方法,都提供多种基本数据类型及Object类行参数的重载方法
sort(int a[])
sort(Object a[])
<T> void sort(T a[],Comparator<?superT> c)

binarySearch(int a[],int key)
binarySearch(Object a[],Object key)
..Comparator

## 4.4 泛型
? extends T //?表示T及其任意一种子类型 上界
? super T //?表示T及其任意一种父类型   下界



# 第五章 异常处理
### 5.1.2 错误和异常
1. 错误
值程序运行时遇到的硬件错误,或操作系统,虚拟机等系统软件错误,或操作错误.
程序本身不能处理错误,只能依靠外界干预.

java.lang.Eroor 是错误类
当运行没有main() 方法的类时,则产生NoClassDefFOundError类
new 申请分配内存时,如果没有可用内存,则产生OutOfMeoryError 内存溢出错误

2. 异常
java.lan.Exception 异常类


# 第六章 图像用户界面

# 第七章 多线程

# 第八章 输入/输出流和文件操作

# 第九章 网络通信

# 第十章 数据库应用

# 第十一章 Web应用

# 第十二章 综合应用设计