# Series
`pandas series` 类似表格中的一个列(`column`)，类似一维数组，可以保存任何数据类型。

## Series 特点：
 - **一维数组**：`series`是一维的，这意味着他只有一个轴(或维度)，类似`Python`中的列表。
 - **索引**：每个`Series` 都有一个索引，它可以是整数，字符串，日期等类型。如果不指定索引，`Pandas`将默认创建一个从0开始的整数索引。
 - **数据类型**：`Series` 可以容纳不同的数据类型的元素，包括整数，浮点数，字符串，`Python`对象等。
 - **操作**：`Series`支持各种操作，如数学运算，统计分析，字符串处理等。
 - **缺失数据**：`Series`可以包含缺失数据，`Pandas`使用`NaN`来表示缺失或无值。
## 创建Series
 可以使用`pd.Series()`构造函数创建一个`Series`对象，传递一个数据数组(可以是列表，`NumPy`数组)和一个可选的索引数组。
 ```python
 pandas.Series(data=None, index=None, dtype=None, name=None, copy=False, fastpath=False)
```
**参数说明**：
- **data**： `Series` 的数据部分，可以用列表，数组，字典，标量值等。如果不提供此参数，则创建一个空的`Series`。
- **index**： `Series` 的索引部分，用于对数据进行标记。可以是列表，数组，索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- **datype**：指定 `Series` 的数据类型。可以是`NumPy`的数据类型，例如 `np.int64`、`np.float64` 等。如果不提供此参数，则根据数据自动推断数据类型。
- **name**：`Series` 的名称，用于标识 `Series` 对象。如果提供了此参数，则创建的 `Series` 对象将具有指定的名称。
- **fastpath**：是否启用快速路径。默认为 `False`。启用快速路径可能会在某些情况下提高性能。

**创建一个简单的Series实例**
```python
import pandas as pd    
a = [1, 2, 3]  
myvar = pd.Series(a)  
print(myvar)
'''
输出结果
0    1
1    2
2    3
dtype: int64
'''
```
**如果没有指定索引，索引值就从 0 开始，我们可以根据索引值读取数据：**
```python
import pandas as pd  
  
a = [1, 2, 3]  
  
myvar = pd.Series(a)  
  
print(myvar[1])
'''
输出结果
2
'''
```
**我们可以指定索引值，如下实例：**
```python
import pandas as pd
a = ['goole', 'runoob', 'wiki']  
myvar = pd.Series(a, index = ['x', 'y', 'z'])  
print(myvar)

'''
输出结果
x     goole
y    runoob
z      wiki
dtype: object
'''
```
**根据索引值读取数据:**
```python
import pandas as pd    
a = ["Google", "Runoob", "Wiki"]    
myvar = pd.Series(a, index = ["x", "y", "z"])    
print(myvar["y"])
'''
输出结果
Runoob
'''
```
**我们也可以使用`key/value` 对象，类似字典来创建 `Series`：**
```python
import pandas as pd    
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}    
myvar = pd.Series(sites)    
print(myvar)
'''
输出结果
1    Google
2    Runoob
3      Wiki
dtype: object 
'''
```
字典的 `key` 变成了索引值。
**如果我们只需要字典中的一部分数据，只需要指定需要数据的索引即可，如下实例：**
```python
import pandas as pd 
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}   
myvar = pd.Series(sites, index = [1, 2])  
print(myvar)
'''
输出结果
1    Google
2    Runoob
dtype: object
'''
```
**设置 `Series` 名称参数：**
```python
import pandas as pd  
sites = {1: "Google", 2: "Runoob", 3: "Wiki"}  
myvar = pd.Series(sites, index = [1, 2], name="RUNOOB-Series-TEST" )  
print(myvar)

'''
输出结果
1    Google
2    Runoob
Name: RUNOOB-Series-TEST, dtype: object
'''
```

# 更多Series说明
**使用列表、字典或数组创建一个默认索引的 Series。**
```python
# 使用列表创建 Series
s = pd.Series([1, 2, 3, 4])

# 使用 NumPy 数组创建 Series
s = pd.Series(np.array([1, 2, 3, 4]))

# 使用字典创建 Series
s = pd.Series({'a': 1, 'b': 2, 'c': 3, 'd': 4})
```
**基本操作：**

```python 
# 指定索引创建 Series
s = pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])

# 获取值
value = s[2]  # 获取索引为2的值
print(s['a'])  # 返回索引标签 'a' 对应的元素

# 获取多个值
subset = s[1:4]  # 获取索引为1到3的值

# 使用自定义索引
value = s['b']  # 获取索引为'b'的值

# 索引和值的对应关系
for index, value in s.items():
    print(f"Index: {index}, Value: {value}")


# 使用切片语法来访问 Series 的一部分
print(s['a':'c'])  # 返回索引标签 'a' 到 'c' 之间的元素
print(s[:3])  # 返回前三个元素

# 为特定的索引标签赋值
s['a'] = 10  # 将索引标签 'a' 对应的元素修改为 10

# 通过赋值给新的索引标签来添加元素
s['e'] = 5  # 在 Series 中添加一个新的元素，索引标签为 'e'

# 使用 del 删除指定索引标签的元素。
del s['a']  # 删除索引标签 'a' 对应的元素

# 使用 drop 方法删除一个或多个索引标签，并返回一个新的 Series。
s_dropped = s.drop(['b'])  # 返回一个删除了索引标签 'b' 的新 Series

```
**基本运算：**
```python
# 算术运算
result = series * 2  # 所有元素乘以2

# 过滤
filtered_series = series[series > 2]  # 选择大于2的元素

# 数学函数
import numpy as np
result = np.sqrt(series)  # 对每个元素取平方根
```
**计算统计数据：使用 Series 的方法来计算描述性统计**
```python
print(s.sum())  # 输出 Series 的总和
print(s.mean())  # 输出 Series 的平均值
print(s.max())  # 输出 Series 的最大值
print(s.min())  # 输出 Series 的最小值
print(s.std())  # 输出 Series 的标准差
```
**属性和方法：**
```python
# 获取索引
index = s.index

# 获取值数组
values = s.values

# 获取描述统计信息
stats = s.describe()

# 获取最大值和最小值的索引
max_index = s.idxmax()
min_index = s.idxmin()

# 其他属性和方法
print(s.dtype)   # 数据类型
print(s.shape)   # 形状
print(s.size)    # 元素个数
print(s.head())  # 前几个元素，默认是前 5 个
print(s.tail())  # 后几个元素，默认是后 5 个
print(s.sum())   # 求和
print(s.mean())  # 平均值
print(s.std())   # 标准差
print(s.min())   # 最小值
print(s.max())   # 最大值
```
**使用布尔表达式：根据条件过滤 Series。**
```python
print(s > 2)  # 返回一个布尔 Series，其中的元素值大于 2
```
**查看数据类型：使用 dtype 属性查看 Series 的数据类型。**
```python
print(s.dtype)  # 输出 Series 的数据类型
```
**转换数据类型：使用 astype 方法将 Series 转换为另一种数据类型。**
```python
s = s.astype('float64')  # 将 Series 中的所有元素转换为 float64 类型
```

>**注意事项：**
>- `Series` 中的数据是有序的。
>- 可以将 `Series` 视为带有索引的一维数组。
>- 索引可以是唯一的，但不是必须的。
>- 数据可以是标量、列表、NumPy 数组等。
