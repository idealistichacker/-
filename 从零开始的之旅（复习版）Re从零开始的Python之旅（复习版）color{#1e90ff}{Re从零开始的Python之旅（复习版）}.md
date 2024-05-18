#  $\color{#1e90ff}{Re:从零开始的Python之旅（复习版）}$

## 一.基础知识：

  ### 1.变量
>
> 1. 变量=值，变量是可以赋给值的标签，也可以说变量指向特定的值。官方：当把一个数据赋值给一个名字时，它会存储在内存中，把这块内存称为变量（variable）。
>
> 2. 变量名只能包含字母、数字和下划线。变量名能以字母或下划线打头，但不能以数字
>     打头。例如，可将变量命名为message_1 ，但不能将其命名为1_message 。
>     ● 变量名不能包含空格，但能使用下划线来分隔其中的单词。例如，变量名
>     greeting_message 可行，但变量名greeting message 会引发错误。
>     ● 不要将Python关键字和函数名用作变量名，即不要使用Python保留用于特殊用途的单
>     词，如print （请参见附录A.4）。
>     ● 变量名应既简短又具有描述性。例如，name 比n 好，student_name 比s_n 好，
>     name_length 比length_of_persons_name 好。
>     ● 慎用小写字母l 和大写字母O ，因为它们可能被人错看成数字1 和0 。
>
>​       ● 区分大小写
>
>3. Python中每一个对象都有三个基本属性：1.唯一标志（对象创建时就有，不可被修改，也不会重复） 2.类型 3.值

  ### 2.简单数据类型
>
>
>
>  ![python的数据类型](D:\A石油大学\学习资料\python\python数据类型.jpg)

  ### 3.运算符
>
> - [ ] 赋值运算符（=）
> - [ ] 算术运算符（+ - * / % ** //）
> - [ ] 关系运算符 (== != <= >=  < >)
> - [ ] 逻辑运算符(and or not)
> - [ ] 成员运算符(in   not in)
> - [ ] 身份运算符(is   is not)
> - [ ] 位运算符(进行二进制位的运算【略】)
>
> 运算符优先级:
>
> | 优先级顺序 | 1    | 2    | 3        | 4    | 5     | 6    | 7    | 8    | 9    | 10   | 11   | 12   | 13   |
> | ---------- | ---- | ---- | -------- | ---- | ----- | ---- | ---- | ---- | ---- | ---- | ---- | ---- | ---- |
> | 运算符     | **   | ~+-  | * / % // | + -  | >> << | &    | ^ \| |      |      |      |      |      |      |
> | 说明       |      |      |          |      |       |      |      |      |      |      |      |      |      |
>
> ![](D:\A石油大学\学习资料\python\运算符优先级.jpg)

  ### 4.输入输出

> `print(values,sep,end,file)`
>
> **格式化输出：**
>
> 1. %：![格式化输出](D:\A石油大学\学习资料\python\python格式化输出1.jpg)
>
>    ![](D:\A石油大学\学习资料\python\python格式化输出2.jpg)

> 2. format:
>
>    ```python
>    name=Tom
>    age=18
>    print('名字:{},年龄:{}'.format(name,age))
>    print('名字:{0},年龄:{1}'.format(name,age))
>    -------------------------------------------
>    print('名字:{name},年龄:{age}'.format(name='Tom',age=18))
>    ```
>
>    ![](D:\A石油大学\学习资料\python\python格式化输出3.jpg) 
>    ```python
>    x='我想'
>    y='爱世界'
>    c=100
>    d=5
>    print('{0:!<8s}{1:!<8s}{2:,.3f}'.format(x+y,y,(c*d)**2))
>    ```
> 	效果：`我想爱世界!!!爱世界!!!!!250,000.000`
>
> 	3. f:
>
> 	 ```python
> 	   name=Tom
> 	   age=18
> 	   print(f'名字:{name},{name}的年龄:{age}')
> 	 ```
>
> **输入**：
>
> 1. `x=input()` `x=eval()`

## ?常用数据类型：

  ### 1.字符串:

#### $杂七杂八：

> 1. *字符串数据进行比较运算时，按照其编码值进行比较。（Unicode编码）*
> 2. *字符串和元组一样为不可变对象，一般对字符串的操作都是存了一个新的字符串*
> 3. *一行代码里尽量不要将TAB与空格混用*
> 4. *new_str=str.??()*
> 5. *str.upper().isupper()从左到右依次调用方法*
> 6. 
>
 #### 1.1 修改大小写：
>
>  ```python
> str.title() #每个单词首字母大写，其它字母小写（方法title() 出现在这个变量的后面。方法 是Python可对数据执行的操作。）
>  str.lower() #全部小写
>  str.upper() #全部大写
>  str.capitalize() #第一个单词首字母大写
>  str.casefold() #全部字母小写，upper只支持英语，而casefold支持其它语言比如德语
>  str.swapcase() #大小写字母翻转
>  ```
 #### 1.2 左中右对齐：
> ```python
> str.center(width,'fillchar')
> str.rjust(width,'fillchar')
> str.ljust(width,'fillchar')
> str.zfill(width) #默认在左边填充0，做报表时常用
> ```
 #### 1.3 字符串的查找：
>  ```python
>  str.count('target str',start,end) #查找某一字符在字符串中出现的次数
>  str.find('sub',strat,end) #从左起获得子字符串在字符串中第一次出现的索引下标值，无则返回-1
>  str.rfind('sub',strat,end) #从右起获得子字符串在字符串中第一次出现的索引下标值，无则返回-1
>  str.index('sub',start,end)#从左起获得子字符串在字符串中第一次出现的索引下标值，无则报错
>  str.index('sub',start,end)#从右起获得子字符串在字符串中第一次出现的索引下标值，无则报错
> 
>  ```
 #### 1.4 字符串的替换：
>  ```python
>  str.expandtabs(int) #将int个空格替换为一个TAB
>  str.replace('old','new','替换次数')
>  table = str.maketrans('ABCDEFG','1234567','将指定的字符串忽略') #属于字符串的一个静态方法
>  n = 'I love FishC'.translate(table) #返还一个根据table表格转换规则、转换后的新字符串
>  print(n)
> 效果:I love 6ishc
>  ```
 #### 1.5 对字符串的判断(返回布尔类型的值)：
> ```python
> str.startswith('target str',起始索引，结束索引)
> str.endswith('target str',起始索引，结束索引)
> str.endswith(('target str1','target str2','target str3')三者之一匹配成功即为真)
> str.istitle() #判断所有单词是否都以大写字母开头
> str.isupper() #判断所有字母是否大写
> str.islower() #判断所有字母是否小写
> str.isalpha() #判断字符串是否全由字母构成
> str.isspace() #判断字符串是否为一个空白字符串（空格 tab \n 均为空白字符）
> str.isprintable() #判断字符串是否全为可打印字符（\n为不可打印字符）
> str.isdecimal() #'2²'返回False、罗马字符、中文数字返回False
> str.isdigit() #罗马字符、中文数字返回False
> str.isnumeric() #普遍性最好
> #以上方法均可判断一个字符串是否为数字、但作用范围不同，其中.isnumeric()方法范围最广
> str.isalnum() #集大成者，在7、10、11、12行的方法中任一一个返回Ture即为Ture。
> str.isidentifier() #判断字符串是否为一个合法的Python标识符，例如给变量起名时就得用合法的Python标识符
> #
> import keyword
> keyword.iskeyword('str')#判断一个字符串是为Python的保留标识符，如 if while 等
> #
> ```
#### 1.6字符串的截取拆分与拼接
> ```python
> str.strip('target str')#在字符串两边截掉包含于目标字符串中的全部字符
> str.lstrip('target str')#在字符串左边截掉包含于目标字符串中的全部字符
> str.rstrip('target str')#在字符串右边截掉包含于目标字符串中的全部字符
> str.removeprefix('target str')#在字符串左边截掉目标字符串
> str.removesuffix('target str')#在字符串右边截掉目标字符串
> str.partition('sep')#从左边起对第一个指定的拆分符对字符串进行拆分，并以一个三元组的形式返回结果
> str.rpartition('sep')#从右边起对第一个指定的拆分符对字符串进行拆分，并以一个三元组的形式返回结果
> str.split('sep=None,maxsplit=-1')#从左起对字符串根据指定拆分符进行拆分，可指定拆分符（默认空格）、拆分次数（默认无限）
> str.rsplit('sep=None,maxsplit=-1')#从右起对字符串根据指定拆分符进行拆分，可指定拆分符（默认空格）、拆分次数（默认无限）
> str.splitlines()#将字符串按行进行分割，并以列表形式返回结果，默认结果不包含换行符如果改为True则包含
> '连接的符号'.join(元组、列表)#执行效率非常高
> ```
#### 1.7格式化字符串
>```python
>'{},{}'.format()
>```

### 2.元组:
#### 1.针对序列都有以下操作： 

> ~~~python
>s='fishc'
> a,b,*c = s
> print(a,b,c)
> ~~~
> 
> 效果：`'f' 'i' ['s','h','c']`
>
#### 2.元组并非固若金汤,如果元组中存放可修改对象是能够被修改的
>
> ~~~python
>t=([1,2,3],[4,5,6])
> t[0][0]=100
> print(t)
> ~~~
> 效果：`([100, 2, 3], [4, 5, 6])`

### 3.列表

#### 1.增

> ```python
> list.append()
> list.extend()#extend方法的参数必须是一个可迭代对象，直接添加到列表最后一个元素后。
> list.insert(插入位置，将插入的元素)
> 
> ```

#### 2.删

> ```python
> list.remove()#删掉列表中第一个匹配的元素，指定的元素不存在会报错
> list.pop(索引)#弹出指定索引的元素
> list.clear()#清空列表中的元素
> 
> 
> ```
>
> 

#### 3.改

> ```python
> list.sort(key=None,reverse=False)#默认从小到大排序，reverse=True则从大到小排序
> list.reverse()#翻转顺序
> ```
>
> 

#### 4.查

> ```python
> list.count()#查找某一元素出现的次数
> list.index(目标索引值，start，end)#查找某一元素的索引值，返回第一次找到的索引值
> list.copy()#拷贝列表
> 
> ```
>
> 

#### 5.嵌套列表

> Python中的赋值操作是将数据与变量进行挂钩，数据是不会变的只是将数据打上了一个个名为“变量”的标签。每次访问数据都是通过变量这个“标签”去寻找罢了。将变量与数据挂钩的行为称为引用。
>
> ~~~python
> x = [1,2,3]
> y = x
> x[1] = 1
> print(x)
> # 此时打印结果为 [1,1,3]
> print(y)
> # 此时打印结果为[1,1,3]
> ~~~
>
> 所以想要只更改x的值而不影响y我们便需要copy（拷贝）这个方法，拷贝分为浅拷贝和深拷贝两种。浅拷贝只适用于一维列表。
>
> ~~~python
> # 以下为浅拷贝的两种方法：
> y = x.copy()
> y = x[:]
> # 切片和x.copy（）都能创建一个独立的y
> ~~~
>
> 浅拷贝只能拷贝外层对象，而对嵌套内部的对象无能为力、对内拷贝的只是其引用。
>
> ~~~python
> # 例如：
> x = [[1,2,3],[4,5,6],[7,8,9]]
> y = x.copy()
> x[1][1] = 0
> print(x)
> # 输出结果为：[[1,2,3],[4,0,6],[7,8,9]]
> print(y)
> # 输出结果同为：[[1,2,3],[4,0,6],[7,8,9]]
> ~~~
>
> 实现深拷贝可以用copy包的函数deepcopy（）实现
>
> ```python
> import copy
> y = copy.deepcopy(x)

#### 6.列表推导式：

~~~python
oho = [1, 2, 3, 4, 5, 6]
oho_change = [i*2 for i in oho]
print(oho_change)
# 輸出爲 [2, 4, 6, 8, 10, 12]
~~~

列表推導式通常比for循環快一倍左右的速度，因爲列表推導式在解釋器裏是以更快的c語言的速度來運行的，因此比使用以步進速度來運行for循環的pythton脚本的虛擬機pvm快很多。



### 4.序列

元组、字典、列表、字符串等可迭代对象都为序列。

#### 序列的特点

Python中的序列是一种基础且强大的数据类型，包括列表（list）、元组（tuple）、字符串（str）和字节串（bytes）。以下是一些序列的常见用法：

1. **创建序列**：
   - 列表：`my_list = [1, 2, 3]`
   - 元组：`my_tuple = (1, 2, 3)`
   - 字符串：`my_string = "hello"`
   - 字节串：`my_bytes = b"hello"`

2. **访问元素**：
   - 使用索引访问：`element = my_list[0]`
   - 使用切片操作访问序列的一部分：`sub_list = my_list[1:3]`

3. **修改元素**：
   - 列表中的元素可以修改：`my_list[1] = 4`

4. **添加元素**：
   - 使用`append()`向列表末尾添加一个元素：`my_list.append(4)`
   - 使用`insert()`在指定位置插入一个元素：`my_list.insert(1, 'a')`
   - 使用`extend()`或`+`合并两个列表：`my_list.extend([4, 5])`
   - 字符串和元组是不可变的，不能直接修改或添加元素。

5. **删除元素**：
   - 使用`del`删除指定位置的元素：`del my_list[1]`
   - 使用`remove()`删除指定值的第一个匹配项：`my_list.remove(3)`
   - 使用`pop()`删除并返回指定位置的元素：`last_element = my_list.pop()`

6. **序列长度**：
   - 使用`len()`函数获取序列的长度：`length = len(my_list)`

7. **序列遍历**：
   - 使用`for`循环遍历序列中的每个元素：`for item in my_list: print(item)`

8. **序列排序**：
   - 使用`sort()`方法对列表进行原地排序：`my_list.sort()`
   - 使用`sorted()`函数返回一个新的排序列表，而不改变原列表：`sorted_list = sorted(my_list)`

9. **序列搜索**：
   - 使用`index()`方法查找值第一次出现的索引：`index = my_list.index(3)`
   - 使用`count()`方法计算某个元素在序列中出现的次数：`count = my_list.count(2)`

10. **序列拼接**：
    - 使用`+`操作符连接两个序列：`new_list = my_list + [4, 5]`

11. **序列解包**：
    - 将序列中的元素赋值给多个变量：`a, b, c = my_tuple`

12. **序列推导式**：
    - 使用简洁的语法创建新序列：`squared_list = [x**2 for x in range(10)]`

13. **序列比较**：
    - 比较操作符（`<`, `<=`, `>`, `>=`, `==`, `!=`）可以用于比较序列。

14. **序列内置函数**：
    - `min()`和`max()`函数可以找到序列中的最小和最大值。
    - `sum()`函数可以计算序列中所有元素的和。

15. **序列格式化**：
    - 使用字符串的`format()`方法或f-string格式化序列。

这些是Python中序列的一些基础用法。Python的序列非常灵活，支持许多其他高级操作，如列表推导式、集合操作等。

#### 序列的常用函数

```python
# 序列可用'+' and '*' ; not in and in ; 切片 ; for循环 ; del
y = [1,2,3,4,5]
y[1:4] = []
# 结果为[1,5]
x = [1,2,3,4,5]
del x[::2]
# 结果为[3,4] 切片无法做到
str(),tuple(),list(),min(,default = ),max(,default = )【设置default 避免传入空序列时报错】,min() 与 max() 也可直接传入多个参数比较大小. 
len(),sum(,start = ) len()有最大可承受范围，32位平台为2^31-1,64位平台为2^63-1
sorted(,key = '传入某种干预排序算法的函数',reverse = ,), 
reversed() 返回参数的反向迭代器
any()任意一个为真则返回True
all()全为真则返回True
enumerate()为序列创建一个枚举对象
zip()创建一个可聚合多个可迭代对象的迭代器；zip()只根据最短的序列来生成迭代器，会自动丢掉多余的值。想要根据最长序列生成迭代器可导入itertools模块，利用其中的zip_longest()函数。
map()根据提供的函数对指定的可迭代对象中的每个元素进行运算并返回一个运算结果的迭代器。
filter()与map()类似，只不过只返回运算结果为真的对象。
iter()将一个序列转换为迭代器
next(,default = '掏空了')，当迭代器空了时可用default避免po

```



### 5.字典

Python字典（dict）是一种内置的数据结构，用于存储键值对。字典提供了多种方法来执行各种操作，包括添加、删除、查找和修改键值对。以下是一些Python字典的常用方法：

1. `dict.get(key, default=None)`

- **用途**：检索字典中键对应的值。如果键不存在，则返回`default`指定的默认值，或者如果未提供`default`，则返回`None`。

- **示例**：

  ```python
  my_dict = {'a': 1, 'b': 2}
  value = my_dict.get('a')  # 返回 1
  value = my_dict.get('c', 'default')  # 返回 'default'
  ```

2. `dict.keys()`

- **用途**：返回一个包含字典所有键的视图对象。

- **示例**：

  ```python
  my_dict = {'a': 1, 'b': 2}
  keys = my_dict.keys()  # 返回 dict_keys(['a', 'b'])
  ```

3. `dict.values()`

- **用途**：返回一个包含字典所有值的视图对象。

- **示例**：

  ```python
  my_dict = {'a': 1, 'b': 2}
  values = my_dict.values()  # 返回 dict_values([1, 2])
  ```

4. `dict.items()`

- **用途**：返回一个包含字典所有键值对的视图对象。

- **示例**：

  ```python
  my_dict = {'a': 1, 'b': 2}
  items = my_dict.items()  # 返回 dict_items([('a', 1), ('b', 2)])
  ```

5. `dict.update(*args, **kwargs)`

- **用途**：将一个或多个字典的键值对更新到当前字典中。如果当前字典中已有相同的键，则值会被新的值覆盖。

- **示例**：

  ```python
  my_dict = {'a': 1, 'b': 2}
  my_dict.update({'b': 3, 'c': 4})  # my_dict 现在是 {'a': 1, 'b': 3, 'c': 4}
  ```

6. `dict.pop(key, default=None)`

- **用途**：删除字典中指定的键值对，并返回该键对应的值。如果键不存在，则返回`default`指定的默认值，或者如果未提供`default`，则抛出`KeyError`。

- **示例**：

  ```python
  my_dict = {'a': 1, 'b': 2}
  value = my_dict.pop('a')  # 删除键 'a' 并返回 1
  value = my_dict.pop('c', 'default')  # 返回 'default'，不抛出错误
  ```

7. `dict.popitem()`

- **用途**：删除字典中的一个任意键值对（默认是最后一个插入的项），并返回该键值对。

- **示例**：

  ```python
  my_dict = {'a': 1, 'b': 2}
  key_value_pair = my_dict.popitem()  # 删除并返回 ('b', 2)
  ```

8. `dict.clear()`

- **用途**：移除字典中的所有键值对。

- **示例**：

  ```python
  my_dict = {'a': 1, 'b': 2}
  my_dict.clear()  # my_dict 现在为空
  ```

9. `dict.copy()`

- **用途**：创建并返回字典的一个浅拷贝。

- **示例**：

  ```python
  my_dict = {'a': 1, 'b': 2}
  new_dict = my_dict.copy()  # new_dict 是 my_dict 的一个副本
  ```

10. `dict.fromkeys(keys, value=None)`

- **用途**：创建一个新字典，其键来自`keys`迭代器，所有键对应的值都设置为`value`（如果未提供`value`，则默认为`None`）。

- **示例**：

  ```python
  keys = ['a', 'b', 'c']
  new_dict = dict.fromkeys(keys, 0)  # 返回 {'a': 0, 'b': 0, 'c': 0}
  ```

11. `dict.setdefault(key, default=None)`

- **用途**：如果字典中存在指定的键，则返回该键对应的值；如果不存在，则向字典中添加该键，并将其值设置为`default`。

- **示例**：

  ```python
  my_dict = {'a': 1}
  value = my_dict.setdefault('a', 2)  # 返回 1，不改变原字典
  value = my_dict.setdefault('b', 2)  # 返回 2，my_dict 现在变成了 {'a': 1, 'b': 2}
  ```

这些方法提供了字典操作的灵活性和强大功能，使得字典成为Python中处理键值对数据的理想选择。在实际编程中，根据具体需求选择合适的方法来操作字典是非常重要的。



## ?常用函数：

### 1.常用内置数学函数：

> ![](D:\A石油大学\学习资料\python\python常用内置函数.jpg)

### 2.如何导入标准函数库

> 1.`import 函数库名 [as 别名]`
>
> 使用这种方法导入函数库后，调用库中的函数时需要在函数名前加上库名作为前缀。
>
> ```python
> import math 
> math.pow(3,2)
> ```
>
> 2.`from 模块名 import *`
>
> `pow(3,2)`
>
> 导入库中所有函数
>
> 3.`from 函数库 import 函数名[as 别名]`
>
> 从库中导入特定函数

清华cmd安装第三方包地址：pip install -i https://pypi.tuna.tsinghua.edu.cn/simple 包名

### 3.常用内置函数

> `dir()`

## 二.OOT

### $杂记：

#### $1.1

1.object-oriented-programming,学好的关键——像上帝一样思考问题

2.面向对象也是一种代码封装的方法——将相关的数据和实现的函数封装到了一起

3.Python中对象=属性+方法（属性即为一个对象的静态特征、方法即为一个对象所能做的事情）

4.在创建对象之前首先要创建一个类（class）

5.在类名中一般第一个字母要大写

6.属性就是写在类里面的变量、方法就是写在类里面的函数

7.封装是面向对象编程的三个基本特征之一（另外2个为继承和多态）



## 三.杂记

​	异常是可控的错误是不可控的。



##### 理解迭代器

迭代器是一次性的，迭代对象一定是迭代器，迭代对象可重复使用。

可直接作用于`for`循环的数据类型如`list`、`tuple`、`dict`等统称为可迭代对象:`Iterable`。使用`isinstance()`可以判断一个对象是否是可迭代对象。例如：

```python
from collections import Iterable
result = isinstance([],Iterable)print(result)
result = isinstance((),Iterable)print(result)
result = isinstance('python',Iterable)print(result)
result = isinstance(213,Iterable)print(result)
```

结果为：

```python
True
True
True
False
```

迭代器的优点

- 迭代器访问与`for`循环访问非常相似，但是也有不同之处。对于支持随机访问的数据结构如元组和列表，迭代器并无优势。因为迭代器在访问的时候会丢失数据索引值，但是如果遇到无法随机访问的数据结构如集合时，迭代器是唯一访问元素的方式；
- 迭代器仅仅在访问到某个元素时才使用该元素。在这之前，元素可以不存在，所以迭代器很适用于迭代一些无法预先知道元素总数的巨大的集合；
- 迭代器提供了一个统一的访问集合的接口，定义`iter()`方法对象，就可以使用迭代器访问。

可以被`next()`函数调用并不断返回下一个值的对象称为迭代器:`Iterator`。`next()`函数访问每一个对象，直到对象访问完毕，返回一个`StopIteration`异常。使用`isinstance()`可以判断一个对象是否是`Iterator`对象。例如：

```python
from collections import Iterator
result = isinstance([],Iterator)print(result)
result = isinstance((),Iterator)print(result)
result = isinstance((x for x in range(10)),Iterator)
print(result)
```

结果为：

```python
False
False
True
```

所有的`Iterable`都可以通过`iter()`函数转化为`Iterator`。

定义迭代器

当自己定义迭代器时，需要定义一个类。类里面包含一个`iter()`函数，这个函数能够返回一个带`next()`方法的对象。例如：

```
class MyIterable:    def __iter__(self):        return MyIterator()class MyIterator:    def __init__(self):        self.num = 0    def __next__(self):        self.num += 1        if self.num >= 10:            raise StopIteration        return self.num
```

复制迭代器

迭代器当一次迭代完毕后就结束了，在此调用便会引发`StopIteration`异常。如果想要将迭代器保存起来，可以使用复制的方法:`copy.deepcopy():x = copy.deepcopy(y)`，不可使用赋值的方法，这样是不起作用的。 

如果您想了解更多迭代器的相关知识，请参考：`[美] Wesley J.Chun 著《 Python 核心编程》`第八章。



python安装目录中的Script是管pip安装包的，需要加入环境变量中；而python安装目录本身是管python解释器的，也得加入环境变量中。





### os.path.splitext()的用法

`os.path.splitext()` 函数是 Python 中 `os` 模块的一部分，它用于将文件路径中的文件名和文件扩展名分离。该函数接受一个参数 `path`，这个参数是一个字符串，表示文件的完整路径。函数返回两个值：第一个是文件名（不含扩展名），第二个是文件的扩展名（包括点号）。

以下是 `os.path.splitext(path)` 函数的详细用法和具体示例：

语法

```python
filename, file_extension = os.path.splitext(path)
```

- `path`：文件的完整路径字符串。
- `filename`：返回的文件名，不包含扩展名。
- `file_extension`：返回的文件扩展名，包括点号。

示例

假设我们有一个名为 `example.txt` 的文件，我们想要分离文件名和扩展名。

```python
import os

# 假设我们有一个文件路径
file_path = 'example.txt'

# 使用 os.path.splitext() 分离文件名和扩展名
file_name, file_extension = os.path.splitext(file_path)

# 输出结果
print(f"文件名: {file_name}")
print(f"文件扩展名: {file_extension}")
```

运行上述代码，输出将会是：
```
文件名: example
文件扩展名: .txt
```

处理带有目录的文件路径

如果文件路径中包含目录，`os.path.splitext()` 函数只会处理最后一个部分，即文件名和它的扩展名。

```python
# 假设我们有一个带目录的文件路径
file_path_with_directory = 'folder/subfolder/example.txt'

# 使用 os.path.splitext() 分离文件名和扩展名
file_name, file_extension = os.path.splitext(file_path_with_directory)

# 输出结果
print(f"文件名: {file_name}")
print(f"文件扩展名: {file_extension}")
```

运行上述代码，输出将会是：
```
文件名: example
文件扩展名: .txt
```

处理没有扩展名的文件

如果文件名没有扩展名，`os.path.splitext()` 函数会返回文件名和空字符串作为文件扩展名。

```python
# 假设我们有一个没有扩展名的文件
file_without_extension = 'image'

# 使用 os.path.splitext() 分离文件名和扩展名
file_name, file_extension = os.path.splitext(file_without_extension)

# 输出结果
print(f"文件名: {file_name}")
print(f"文件扩展名: {file_extension}")
```

运行上述代码，输出将会是：
```
文件名: image
文件扩展名: 
```

`os.path.splitext()` 函数是一个非常有用的工具，特别是在处理文件时需要区分文件名和文件扩展名进行不同的操作。通过这个函数，我们可以轻松地获取文件的基本名称和它的扩展名，从而进行后续的文件处理工作。



### os模块的一些用法

`os`模块是Python标准库中的一个核心模块，它提供了许多与操作系统交互的函数。使用`os`模块，你可以执行与操作系统相关的任务，如文件和目录操作、进程管理、环境变量设置等。以下是`os`模块的一些详细用法：

1. 文件和目录操作

- **os.getcwd()**: 返回当前工作目录的路径。
  ```python
  import os
  current_directory = os.getcwd()
  print("当前工作目录:", current_directory)
  ```

- **os.chdir(path)**: 更改当前工作目录到指定的路径。
  ```python
  os.chdir("/path/to/directory")
  ```

- **os.listdir(path='.')**: 列出指定目录下的所有文件和子目录名。
  ```python
  entries = os.listdir()
  print("目录内容:", entries)
  ```

- **os.mkdir(path)**: 创建一个新目录。
  ```python
  os.mkdir("/new/directory")
  ```

- **os.makedirs(path)**: 递归创建目录。
  ```python
  os.makedirs("/new/directory/subdir", exist_ok=True)
  ```

- **os.rmdir(path)**: 删除空目录。
  ```python
  os.rmdir("-empty/directory")
  ```

- **os.removedirs(path)**: 递归删除目录。
  ```python
  os.removedirs("/path/to/directory")
  ```

- **os.rename(src, dst)**: 重命名文件或目录。
  ```python
  os.rename("old_name.txt", "new_name.txt")
  ```

- **os.path.exists(path)**: 检查指定路径的文件或目录是否存在。
  ```python
  exists = os.path.exists("file.txt")
  print("文件或目录是否存在:", exists)
  ```

2. 文件操作

- **os.open(file, flags, mode)**: 打开文件，类似于内置的`open()`函数，但提供更多的功能。
  
  ```python
  fd = os.open("file.txt", os.O_WRONLY | os.O_CREAT, 0o644)
  ```
  
- **os.close(fd)**: 关闭一个已打开的文件描述符。
  ```python
  os.close(fd)
  ```

- **os.read(fd, n)**: 从文件描述符读取最多n个字节的数据。
  ```python
  data = os.read(fd, 1024)
  ```

- **os.write(fd, str)**: 将字符串写入到文件描述符指向的文件中。
  ```python
  os.write(fd, b"Hello, World!")
  ```

3. 进程管理

- **os.fork()**: 在类Unix系统上创建一个新进程。在Windows上不可用。
  ```python
  pid = os.fork()
  if pid == 0:
      print("子进程")
  else:
      print("父进程", pid)
  ```

- **os.execvp(file, args)**: 执行一个程序，用给定的参数替换当前进程。
  ```python
  os.execvp("/bin/ls", ["ls", "-l"])
  ```

- **os.wait()**: 等待子进程结束，返回一个包含两个元素的元组（pid, status）。
  ```python
  pid, status = os.wait()
  ```

4. 环境变量

- **os.environ**: 一个包含环境变量的映射对象。
  ```python
  path = os.environ.get("PATH")
  print("PATH环境变量:", path)
  ```

- **os.putenv(key, value)**: 设置环境变量的值。
  ```python
  os.putenv("MY_VAR", "value")
  ```

- **os.unsetenv(key)**: 删除一个环境变量。
  ```python
  os.unsetenv("MY_VAR")
  ```

5. 其他有用的函数

- **os.getuid()**: 获取当前进程的用户ID。
  ```python
  uid = os.getuid()
  print("用户ID:", uid)
  ```

- **os.getpid()**: 获取当前进程的进程ID。
  ```python
  pid = os.getpid()
  print("进程ID:", pid)
  ```

- **os.getlogin()**: 获取当前登录名。
  ```python
  username = os.getlogin()
  print("登录名:", username)
  ```

- **os.umask(mask)**: 设置文件的默认权限掩码。
  ```python
  os.umask(0o022)
  ```

这些只是`os`模块提供的一部分功能。根据你的需要，你可以探索更多的函数和参数。在使用这些函数时，请确保你了解它们的用法和限制，特别是在处理文件和进程时，因为不当的操作可能会导致数据丢失或安全问题。

`os`模块是Python标准库中提供操作系统接口的模块之一，它包含了许多实用的函数，可以帮助你与操作系统进行交互，执行各种文件和目录相关的操作。以下是`os`模块中一些常用函数的详细介绍和使用示例：

os.listdir()

**功能**：列出指定目录下的所有文件和目录名。

**语法**：
```python
os.listdir(path='.', *, encoding=None)
```
- `path`：要列出内容的目录路径。默认为当前工作目录（'.'）。
- `encoding`：用于解码字节字符串的编码，如果文件名包含非ASCII字符，需要指定。

**示例**：
```python
import os

# 获取当前目录下的所有文件和目录名
entries = os.listdir()
print("目录内容:", entries)
```

os.path.isfile()

**功能**：检验指定路径是否为一个文件。

**语法**：
```python
os.path.isfile(path)
```
- `path`：要检查的文件路径。

**示例**：
```python
import os

# 检查'file.txt'是否为一个文件
is_file = os.path.isfile('file.txt')
print("'file.txt'是否为文件:", is_file)
```

os.path.splitext()

**功能**：分离文件名和扩展名。

**语法**：
```python
os.path.splitext(path)
```
- `path`：文件的路径。

**示例**：
```python
import os

# 分离文件名和扩展名
filename, file_extension = os.path.splitext('report.docx')
print("文件名:", filename)
print("扩展名:", file_extension)
```

os.path.getsize()

**功能**：获取指定文件的大小（单位：字节）。

**语法**：
```python
os.path.getsize(path)
```
- `path`：要获取大小的文件路径。

**示例**：
```python
import os

# 获取'report.docx'文件的大小
file_size = os.path.getsize('report.docx')
print("'report.docx'文件大小（字节）:", file_size)
```

这些函数是`os`模块中与文件和目录操作相关的常用工具。通过它们，你可以编写脚本来自动化文件管理任务，例如列出目录内容、检查文件类型、处理文件名和扩展名以及获取文件大小等。在使用这些函数时，需要注意异常处理，例如处理文件不存在或无法访问的情况。此外，为了确保代码的可移植性，建议使用`os.path.join()`等函数来构建跨平台兼容的路径。

### 相对路径

相对路径是一种文件路径表示方法，它不是使用绝对方式指向文件系统中的固定位置，而是根据当前工作目录（current working directory）来定位文件或目录。相对路径使得文件和代码更加灵活和可移植，因为它们可以在不同的目录结构中轻松移动而不需要修改路径。

相对路径的组成部分

1. **当前目录（`.`）**：表示当前工作目录。
   ```plaintext
   ./file.txt
   ```

2. **父目录（`..`）**：表示当前工作目录的上一级目录。
   ```plaintext
   ../parent_directory/file.txt
   ```

3. **子目录**：直接位于当前工作目录下的目录。
   ```plaintext
   subdir/file.txt
   ```

4. **组合使用**：可以组合使用当前目录、父目录和子目录来形成更复杂的路径。
   ```plaintext
   ../parent/subdir/file.txt
   ```

使用相对路径的注意事项

- **跨平台兼容性**：在类Unix系统（如Linux和macOS）和Windows系统中，路径分隔符可能不同（`/` 对于类Unix系统，`\` 对于Windows）。为了确保兼容性，可以使用`os.path.join()`函数来构建路径，它会根据运行平台自动选择正确的分隔符。
  ```python
  import os
  path = os.path.join('subdir', 'file.txt')
  ```

- **当前工作目录的变化**：在使用相对路径时，需要意识到当前工作目录可能会变化。例如，在运行脚本时，当前工作目录可能是脚本所在的目录，而在交互式解释器中，它可能是启动Python时的目录。

- **避免硬编码**：尽量避免在代码中硬编码相对路径，因为这会降低代码的可维护性和可移植性。可以使用`os.getcwd()`函数获取当前工作目录，或者通过其他方式（如配置文件、环境变量）来指定路径。

示例

假设你的文件系统结构如下：

```plaintext
/home/user/
├── project/
│   ├── main.py
│   └── data/
│       └── results.csv
└── documents/
    └── report.docx
```

如果你在`main.py`中，想要读取`results.csv`文件，可以使用相对路径：

```python
import csv

# 假设当前工作目录是 /home/user/project
# 直接引用当前目录下的文件
with open('data/results.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print(row)

# 引用上一级目录下的文件
with open('../documents/report.docx', 'r') as docfile:
    content = docfile.read()
    print(content)
```

在这个例子中，`'data/results.csv'`是一个相对路径，它指向当前目录下的`data`子目录。而`'../documents/report.docx'`是一个相对路径，它首先上升到上一级目录，然后进入`documents`目录。

相对路径是一种非常实用的文件定位方法，它使得文件和代码更加灵活，便于在不同的环境中运行和维护。

## 大学计算机听讲笔记

### 第三章 数据的获取

#### 网页数据的获取

主要使用两个函数库（Python包）：requests（获取网页内容）、beautifulsoup4（获取目标内容）。

网页的基本结构：ＨＴＭＬ语言（HyperＴｅｘｔ　Ｍａｒｋｕｐ　Language）



网页请求函数requests.get()构造一个请求服务器的request对象，其语法为：

**r = requests.get(url\[,params=None][,\**kwargs]),其中url表示拟获取网页的url**

连接，url链接必须采用HTTP或HTTPS方式访问；params表示url中的额外参数，字典或字节流格式，可选；**kwargs表示12个控制访问的参数均为可选，常使用的参数有timeout、headers、cookies。

**在调用requests.get()函数后，返回的网页内容会保存为一个Response对象r。**



Ｒｅｓｐｏｎｓｅ对象ｒ包含服务器返回的所有信息，也包含请求的Request信息，其常用方法如图所示：

<img src="D:\A石油大学\Typora\计算机\Python 3 网络爬虫 Picture\Response对象r包含的信息.jpg" style="zoom: 33%;" />









ｓｔａｔｕｓ＿ｃｏｄｅ表示服务器的响应状态，２００表示服务器正常响应，４０４代表页面未找到，５００代表服务器内部发生错误。



#### 数据处理与数据分析

Pandas包含的基本数据结构为：Series和DateFrame。可将Pandas理解为一个内存数据库，所有数据全部存放在内存中，每一个DateFrame可看作一个数据库中的表，一个Series可理解为表的一列。DateFrame中的每一行相当于表的一条记录。

Series是一维的类似数组的对象，并且其中的每个元素都有一个索引。它可以包含任何数据类型，如整型、浮点型、字符串、Python对象等。



### 自我补充

#### 杂记：



##### 杂记3 python变量在内存中的一些基本知识

在Python中，变量是存储数据的容器，它们在内存中的行为和表现方式对于理解Python的工作原理至关重要。以下是关于Python变量在内存中的一些基本知识：

1. 变量和对象

在Python中，变量并不实际存储数据，而是存储对数据（对象）的引用。当你创建一个变量并赋值时，你实际上是在变量和对象之间创建了一个引用关系。

2. 内存分配

当一个对象被创建时，Python解释器会在内存中为该对象分配足够的空间来存储它的数据。这个空间的大小取决于对象的类型和内容。例如，字符串、数字、列表、字典等都有自己的内存分配方式。

3. 栈和堆

在Python中，变量名（包括局部变量和全局变量）存储在栈（stack）中，而对象本身通常存储在堆（heap）中。栈用于存储指向对象的引用，而堆用于存储对象本身。

4. 引用计数

Python使用引用计数机制来管理内存。每当你创建一个变量指向一个对象，该对象的引用计数增加。当变量被删除或重新赋值时，引用计数减少。当对象的引用计数降为零时，意味着没有任何变量引用该对象，Python会自动释放该对象占用的内存。

5. 变量的作用域

变量的作用域决定了变量在代码中的可见性和生命周期。局部变量仅在定义它们的函数或代码块中可见，而全局变量在整个程序中都是可见的。局部变量存储在栈中，而全局变量和函数通常存储在堆中。

6. 垃圾回收

Python有一个内置的垃圾回收器，它负责回收不再使用的内存。当对象的引用计数为零时，垃圾回收器会自动释放对象占用的内存。此外，Python的垃圾回收器还可以处理循环引用的情况。

7. 可变类型和不可变类型

Python中的数据类型分为可变类型和不可变类型。不可变类型（如字符串、元组和数字）在被修改时会创建一个新的对象。可变类型（如列表和字典）可以在原地修改，不需要创建新对象。

8. 内存优化

虽然Python的内存管理是自动的，但程序员仍然可以通过编写高效的代码来优化内存使用。例如，使用局部变量、避免不必要的全局变量、使用生成器而不是列表来处理大数据集等。

了解这些基本知识有助于你更好地理解Python代码的行为，以及如何有效地管理内存。这对于编写高效、可扩展的Python应用程序非常重要。







##### 杂记2 if_name_ == '_main_':

今天来写一篇关于Python基础的内容。很多初学Python的小白经常会看到别人写的Python代码中有一句这样的代码：

```text
if __name__ == '__main__':
    # do something
```

看不明白这句话if __name__ == '__main__':是什么意思，__name__和__main__究竟是个什么鬼？今天咱们主要就来讲讲这句话的意思。



![img](https://pic4.zhimg.com/80/v2-ebb6b8b781479810ba1c345337e8779f_1440w.webp)

要想弄明白这句代码的意思，必须先明白在Python中必须知道的两个知识点，如下：



> \1. 在Python中，凡是以两个下划线开头，两个下划线结尾的变量叫做“魔法变量”。瓦特？魔法变量？对，你没有听错，就是魔法变量。当然，如果你觉得这个词不好理解的话，你可以简单地认为所谓魔法变量就是Python对象内置天生就有的属性变量，你使用这些变量前不需要自己去定义，直接用就是。当然，既然是天生就有的，你也别去修改它，正常使用就好。
> \2. Python中每个py文件都叫一个模块。系统里面我们经常导入的模块，比如什么os啊，math啊，这些它们的本质都是一个个的py文件。当然，我们自己写的每个py文件也都是一个个的模块，咱们可以把它看成是一个自定义模块。模块既然就是Python文件，那么它就有两种运行方式：一种是直接运行，另外一种是导入别的模块中再运行。



理解了以上两个知识点，我们再来看看这个语句：

```text
if __name__ == "__main__":
    # do something
```

很明显，要知道这句代码的意思，就必须弄懂__name__和__main__是什么意思。实际上，__name__这个魔术变量存在于Python的每个模块对象中，也就是说，按照我们上面的说法，每个py文件都有一个__name__属性。接下来，我们通过代码来看看这个__name__属性的特性。



我们首先创建一个叫demo.py的Python文件，里面只有一句代码，如下：

```text
print(__name__)
```

如果我们运行一下，看会得到什么结果呢？很简单，结果如下：

![img](https://pic3.zhimg.com/80/v2-1655ad1409d88e3dd56b3ea5504c5506_1440w.webp)

从结果中我们可以看到，直接在某个模块中打印它自己的__name__属性，值就是__main__，这代表当前模块正在以“直接运行”的方式在运行。



接下来，我们再把这个非常简单的模块导入到别的Python文件中，看看会发生什么结果？比如我们重新创建一个文件名字叫study.py，然后在study.py中导入刚刚那个demo.py模块，代码如下：

```text
import demo
```

然后，我们运行这个study.py，看看会发生什么。运行它之后，我们会发现，虽然这个study.py文件中除了导入了一个demo模块外什么都没写，但它却神奇地打印了一个值出来，结果如下：

![img](https://pic3.zhimg.com/80/v2-e63b2a485728573b471468f5775d3bba_1440w.webp)

看到了吧，它打印出了“demo”这个字符串。别急，此时大家脑子里可能有一个疑问，这个“demo”这个字符串怎么来的？对，我们必须搞懂这个问题。



这个问题答案其实很简单，我们只需要明白两点：首先，当模块A被导入到模块B中时，一旦运行模块B，模块A中的语句会自动被执行一遍，以便加载模块A中的所有函数定义啊、类定义等语句到内存中等待被使用。所以，正是基于这个行为，前面例子中运行study.py这个文件时，其实就相当于自动运行了一次demo.py这个文件。第二点，当模块是以“被导入”的方式运行时，它的__name__属性会自动变成该模块的名字，这就是为什么运行study.py打印出来的是“demo”而不是“__main__”的原因。



看到这里，相信大家已经能够了解为什么我们要在定义一个模块时会写if __name__ == "__main__": 这个语句了，这个if语句的条件只有当这个模块被直接运行时才会满足，当这个模块被导入别的模块时是不会被满足的。所以，凡是想让某些代码只在直接执行当前模块时运行，就把这些代码放到这个if语句下面即可，这就是这个语句存在的意义。



我们今天的文章就先到这里，如果大家对文中的知识点有任何疑问，欢迎给我留言，谢谢。

**注：**本文为凡云教育校长卿淳俊老师原创，首发自个人公众号“凡云说”，原文链接[Python中if __name__ == '__main__'的作用是什么](https://link.zhihu.com/?target=https%3A//mp.weixin.qq.com/s/pvbL9IY6jEBsJlj_DD657g)。切勿擅自盗用，如需转载请私聊我处获得授权并注明出处。



##### 杂记1 字典的几种创建方式

在Python中，字典是一种内置的数据结构，它存储键值对（key-value pairs）。字典中的键必须是唯一的，而值则可以是任何数据类型。创建字典有几种不同的方法：

 1. 空字典

首先，你可以通过简单地使用两个大括号 `{}` 来创建一个空字典。

```
my_dict = {}
```

 2. 字典推导式

你可以使用字典推导式来创建一个字典，这种方法通常用于从其他数据结构创建字典，或者根据一些规则生成键值对。

```
 从列表创建字典
my_list = ['apple', 'banana', 'cherry']
my_dict = {item: item.upper() for item in my_list}

 从两个列表创建字典（一对一映射）
keys = ['a', 'b', 'c']
values = [1, 2, 3]
my_dict = {key: value for key, value in zip(keys, values)}
```

 3. 使用键值对

你可以直接在大括号中定义键值对来创建一个字典。

```
my_dict = {'name': 'Alice', 'age': 25, 'location': 'Wonderland'}
```

 4. 使用 `dict()` 构造函数

你还可以使用 `dict()` 构造函数来创建字典。你可以传递一个可迭代对象，如键值对的列表，给这个构造函数。

```
 从键值对列表创建字典
items = [('name', 'Alice'), ('age', 25), ('location', 'Wonderland')]
my_dict = dict(items)

 从两个列表创建字典（一对一映射）
keys = ['name', 'age', 'location']
values = ['Alice', 25, 'Wonderland']
my_dict = dict(zip(keys, values))
```

 5. 使用 `update()` 方法

如果你已经有一个字典，你可以使用 `update()` 方法来添加新的键值对或更新现有的键值对。

```
my_dict = {'name': 'Alice'}
my_dict.update({'age': 25, 'location': 'Wonderland'})
```

 6. 使用 `setdefault()` 方法

`setdefault()` 方法可以用来添加键值对，如果键不存在的话。如果键已经存在，它将返回该键的值而不进行任何更改。

```
my_dict = {'name': 'Alice'}
my_dict.setdefault('age', 25)  # 添加新的键值对 'age': 25
my_dict.setdefault('name', 'Bob')  # 不会更改 'name' 的值，因为它已经存在
```

这些方法提供了灵活多样的方式来创建和修改字典。在实际编程中，你可以根据具体的需求和场景选择最合适的方法。







#### 爬虫基础 HTTP基本原理 

##### 2.１.１　URI 和　URL、URN

ＵＲＩ（Ｕｎｉｆｏｒｍ　Ｒｅｓｏｕｒｃｅ　Ｉｄｅｎｔｉｆｉｅｒ）

ＵＲＬ（Ｕｎｉｆｏｒｍ　Ｒｅｓｏｕｒｃｅ　Ｌｏｃａｔｅｒ）

ＵＲＮ　（Ｕｎｉｆｏｒｍ　Ｒｅｓｏｕｒｃｅ　Ｎａｍｅ）

<img src="D:\A石油大学\Typora\计算机\Picture\URI包含URL 与 URN.png" style="zoom: 50%;" />



一般来说，现在的网页链接基本上都可以称为URI 或URL ，URＬ几乎都是ＵＲＩ。



HTTPS的安全基础是SSL（Sｅｃｕｒｅ　Ｓｏｃｋｅｔ　Ｌａｙｅｒ），通过ｈｔｔｐｓ传输的数据都经过加密，HTTPS的主要作用有两种：

１.建立一个信息安全通道来保证数据传输的安全

２.确立网站的真实性，凡是用了HTTPS的网站，都可以通过点击浏览器网址前的小锁标志来查看网站认证后的真实信息，也可以通过CA机构颁发的安全签章来查询。

##### 2.1.5请求

请求，由客户端向服务器发出，可列为4部分内容：Request Method（请求方法）、Request URL（请求网址）、Request Headers（请求头）、Request Body（请求体）。

1.请求方法：GET and POST

GET请求：将请求的参数直接包含到URL中；例如，百度中搜索Python，链接为：https//：www.baidu.com/s?wd=Python

参数wd表示搜寻的关键字

GET请求提交的数据最多只有1024字节，而POST方式没有限制

POST请求：多在表单提交时发起，如登录界面（登录表单），输完账号、密码后点击“登录”按钮，便会发起一个POST请求，其数据常以表单的形式传输，包含在请求体中，而不会体现在URL中。

2.请求网址：即为URL唯一确定我们请求的资源。

3.请求头：

用来说明服务器要使用的附加信息，比较重要的信息有Cookie、Referer、User——Agent等。

Accept：请求报头域，用于指定客户端可接受哪些类型的信息。

Accept——Language：指定客户端可接受的语言类型

Accept——Encoding：指定客户端可接受的内容编码

Host：用于指定请求资源的主机IP和端口号，其内容为请求URL的原始服务器或网关的位置。从HTTP1.1版本开始，请求必须包含此内容。

4.请求体：

请求体一般承载的内容是POST请求中的表单数据，而对于GET请求，请求体则为空。

在爬虫中，如果要构造POST请求，需要使用正确的Content——Type，并了解各种请求库的各个参数设置时使用的是哪种Content-Type，不然可能导致POST提交后无法正常响应。

##### 2.1.6 响应

响应，由服务端返回给客户端，可以分为三部分：Response Status Code（响应状态码）、Response Headers（响应头）、Response Body（响应体）。

1.响应状态码：404、200、500等。

2.响应头：包含了服务器对请求的应答信息，如Content-Type（MIME、Internet Media Type）、Server、Set-Cookie等。

**3.响应体**：

响应的正文数据都在响应体中，比如请求网页时，它的响应体就是网页的HTML代码；请求一张图片时，它的响应体就是图片中的二进制数据。做爬虫请求网页后要解析的内就是响应体。



以上为HTTP的基本原理



#### 2.2 网页基础

##### 2.2.1网页的组成

网页分为三部分：HTML（骨架）、CSS（皮肤）、JavaScript（肌肉）

**1.HTML（Hyper Text Markup Language）：**

一种语言，通过图片（img）、视频（video）等各种标签和布局标签（div）的组合嵌套形成网页的基本骨架。

**2.CSS(Cascading Style Sheets 层叠样式表):**

层叠：网页中引用了数个样式文件并且样式有冲突时，浏览器根据层叠顺序进行处理。“样式”指网页中的文字大小、颜色、元素间距、排列等格式。

在网页中一般会统一定义整个网页的样式规则，并写入CSS文件中（其后缀为css）。在HTML中，只需要link标签即可引入写好的CSS文件，这就使整个页面美观、优雅。

**3.JavaScript：**

JS是一种脚本语言。实现网页的交互和动画效果例如下载进度条、提示框、轮播图等。JS后缀为js在HTML中通过script便签引入。

##### 2.2.2 网页的结构

##### 2.2.3 节点树及节点间的关系

在HTML中，所有标签定义的内容都是节点，它们构成了一个HTML DOM树。

DOM（Document Object Model）是W3C（万维网联盟）的标准，即文档对象模型。它定义了访问HTML和、XML文档的标准。































  













