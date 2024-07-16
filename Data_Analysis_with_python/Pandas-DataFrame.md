# DataFrame
`DataFrame` 是 `Pandas` 中的另一个核心数据结构，用于表示二维表格型数据。

`DataFrame` 是一个表格型的数据结构，它含有一组有序的列，每列可以是不同的值类型（数值、字符串、布尔型值）。

`DataFrame` 既有行索引也有列索引，它可以被看做由 `Series` 组成的字典（共同用一个索引）。

`DataFrame` 提供了各种功能来进行数据访问、筛选、分割、合并、重塑、聚合以及转换等操作。

## DataFrame 特点：
- **二维结构：** `DataFrame` 是一个二维表格，可以被看做是一个Excel电子表格或sql表，具有行和列。可以将其视为多个`Series`对象组成的字典。
- **列的数据类型：** 不同的列可以包含不同的数据类型，如整数，浮点，字符串或`python`对象等。
- **索引：** `DataFrame` 可以拥有行索引和列索引，类似于`Excel`中的行号和列标。
- **大小可变：** 可以添加和删除列，类似于`Python`中的字典。
- **自动对齐：** 在进行算术运算或数据对齐操作时， `DataFrame` 会自动对齐索引。
- **处理缺失数据：** `DataFrame` 可以包含缺失数据， `pandas` 是要用NaN来表示。
- **数据操作：** 支持数据切片，索引，子集分割等操作。
- **时间序列支持：** `DataFrame` 对时间序列数据有特别的支持，可以轻松的进行时间数据的切片，索引和操作。
- **丰富的数据访问功能：** 通过 `.loc`, `,iloc`,和 `.query()`方法，可以灵活的访问和筛选数据。
- **灵活的数据处理功能：** 包含数据合并，重塑，透视，分组和聚合。
- **数据可视化：** 虽然`DataFrame`本身不是可视化工具，但它可以与`Matplotlib` 或 `Seaborn`等可视化库结合使用，进行数据可视化。
- **高效的数据输入输出：** 可以方便的读取和写入数据，支持各种格式，如`CSV`, `Excel`, `Sql`数据库和HDF5格式。
- **描述性统计：** 提供了一系列方法来计算描述性统计数据，如 `.describe()`, `.mean()`, `.sum()`等
- **灵活的数据对齐和集成：** 可以轻松地与其他`DataFranme` 或 `Series` 对象进行合并，连接或更新操作。 
- **转换功能：** 可以对数据集中的值进行转换，例如使用`.apply()`方法应用自定义函数。
- **滚动窗口和时间序列分析：** 支持对数据集进行滚动窗口统计和时间序列分析。
## DataFrame 构造方法
```python
pandas.DataFrame(data=None, index=None, columns=None, dtype=None, copy=False)

```
**参数说明：**
- `data`: `DataFrame` 的数据部分，可以是字典，二维数组，`Series`, `DataFrame` 或其他可转换为`DataFrame`的对象。如果不提供此参数，则创建一个空的`DataFrame`。
- `index`: `DataFrame` 的行索引，用于标识每行数据。可以是列表，数组，索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- `columns`：`DataFrame`的列索引，用于标识每列数据。可以是列表，数组，索引对象等。如果不提供此参数，则创建一个默认的整数索引。
- `dtype`: 指定`DataFrame`的数据类型。可以是Numpy的数据类型，例如`np.int64`, `np.float64`等。如果不提供此参数，则根据数据自动推断数据类型。
- `copy`：是否复制数据。默认为`False`，表示不复制数据。如果设置为 `True`，则复制输入的数据。

**Pandas DataFrame是一个二维的数据结构，类似二维数组。**
**使用列表创建**
```python
import pandas as pd
data = [['Google', 10], ['Runoob', 12], ['Wiki', 13]]
# 创建DataFrame
df = pd.DataFrame(data, columns=['Site', 'Age'])
# 使用astype方法设置每列的数据类型
df['Site'] = df['Site'].astype(str)
df['Age'] = df['Age'].astype(float)
print(df)
'''
输出结果
     site   age
0  Google  10.0
1  runoob  12.0
2    Wiki  13.0
'''
```
**使用字典创建**
```python
import pandas as pd
data = {'Site':['Google', 'Runoob', 'Wiki'], 'Age':[10, 12, 13]}
df = pd.DataFrame(data)
print (df)
'''
输出结果
     Site  Age
0   Google  10
1  Runoob   12
2    Wiki   13
'''
```
**使用ndarrays创建**
```python
import numpy as np
import pandas as pd
# 创建一个包含网站和年龄的二维ndarray
ndarray_data = np.array([
    ['Google', 10],
    ['Runoob', 12],
    ['Wiki', 13]
])
# 使用DataFrame构造函数创建数据帧
df = pd.DataFrame(ndarray_data, columns=['Site', 'Age'])
# 打印数据帧
print(df)

'''
输出结果
     Site Age
0  Google  10
1  Runoob  12
2    Wiki  13

'''
```
以上实例使用 ndarrays 创建，ndarray 的长度必须相同， 如果传递了 index，则索引的长度应等于数组的长度。如果没有传递索引，则默认情况下，索引将是range(n)，其中n是数组长度。
**使用字典(key/value),其中字典的key为列名：**
```python
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
print (df)
'''
输出结果
   a   b     c
0  1   2   NaN
1  5  10  20.0
'''
```
没有对应的数据部分为NaN
Pandas 可以使用 loc 属性返回指定行的数据，如果没有设置索引，第一行索引为 **0**，第二行索引为 **1**，以此类推：
```python
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行
print(df.loc[0])
# 返回第二行
print(df.loc[1])
'''
输出结果
calories    420
duration     50
Name: 0, dtype: int64
calories    380
duration     40
Name: 1, dtype: int64
'''
```
>**注意：**  返回结果其实一个Pandas Series数据

也可以返回多行数据，使用 `[[ ... ]]` 格式，... 为各行的索引，以逗号隔开：
```python
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
# 数据载入到 DataFrame 对象
df = pd.DataFrame(data)
# 返回第一行和第二行
print(df.loc[[0, 1]])
'''
输出结果
   calories  duration
0       420        50
1       380        40
'''
```
>**注意：** 返回结果其实就是一个 Pandas DataFrame 数据。

我们可以指定索引值，如下实例：
```python
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)
'''
输出结果
      calories  duration
day1       420        50
day2       380        40
day3       390        45
'''
```
Pandas 可以使用 loc 属性返回指定索引对应到某一行：
```python
import pandas as pd
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
# 指定索引
print(df.loc["day2"])
'''
输出结果
calories    380
duration     40
Name: day2, dtype: int64
'''
```

## 更多DataFrame 说明

### 创建DataFrame
- 从字典创建：字典的键成为列名，值成为列数据。
```python
import pandas as pd
# 通过字典创建 DataFrame
df = pd.DataFrame({'Column1': [1, 2, 3], 'Column2': [4, 5, 6]})
```
- 从列表的列表创建： 外层列表代表行，每层列表代表列。
```python 
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                  columns=['Column1', 'Column2', 'Column3'])
'''
输出结果
   Column1  Column2  Column3
0        1        2        3
1        4        5        6
2        7        8        9
'''
```
- 从NumPy数组创建：提供一个二维Numpy数组
```python
import numpy as np
# 通过 NumPy 数组创建 DataFrame
df = pd.DataFrame(np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]]))
```
- 从Series创建DataFrame：通过pd.Series()创建
```python
# 从 Series 创建 DataFrame
s1 = pd.Series(['Alice', 'Bob', 'Charlie'])
s2 = pd.Series([25, 30, 35])
s3 = pd.Series(['New York', 'Los Angeles', 'Chicago'])
df = pd.DataFrame({'Name': s1, 'Age': s2, 'City': s3})
```

### DataFrame 的属性和方法
DataFrame 对象有许多属性和方法，用于数据操作、索引和处理，例如：shape、columns、index、head()、tail()、info()、describe()、mean()、sum() 等。
```python
# DataFrame 的属性和方法
print(df.shape)     # 形状
print(df.columns)   # 列名
print(df.index)     # 索引
print(df.head())    # 前几行数据，默认是前 5 行
print(df.tail())    # 后几行数据，默认是后 5 行
print(df.info())    # 数据信息
print(df.describe())# 描述统计信息
print(df.mean())    # 求平均值
print(df.sum())     # 求和
```

### 访问DataFrame 元素

- 访问列： 使用列名作为属性或通过`.loc[]`, `.iloc[]`访问，也可以使用标签或位置索引
```python
# 通过列名访问
print(df['Column1'])
# 通过属性访问
print(df.Name)        
# 通过 .loc[] 访问
print(df.loc[:, 'Column1'])
# 通过 .iloc[] 访问
print(df.iloc[:, 0])  # 假设 'Column1' 是第一列
# 访问单个元素
print(df['Name'][0])
```
- 访问行：使用行的标签和`.loc[]`访问
```python
# 通过行标签访问
print(df.loc[0, 'Column1'])
```

### 修改DataFrame
- 修改列数据：直接对列进行赋值
```python
df['Column1'] = [10, 11, 12]
```
- 添加新列： 给新列赋值
```python
df['NewColumn'] = [100, 200, 300]
```
添加新行：使用`loc` `append` 或 `concat`方法
```python
# 使用 loc 为特定索引添加新行
df.loc[3] = [13, 14, 15, 16]

# 使用 append 添加新行到末尾
new_row = {'Column1': 13, 'Column2': 14, 'NewColumn': 16}
df = df.append(new_row, ignore_index=True)
```
**注意**：`append()`方法在 pandas 版本 1.4.0 中已经被标记为弃用，并将在未来的版本中被移除，官方推荐使用 `concat()` 作为替代方法来进行数据的合并操作。
`concat()` 方法用于合并两个或多个`DataFrame`，当你想要添加一行到另一个 `DataFrame` 时，可以将新行作为一个新的 `DataFrame`，然后使用 `concat()`：
```python

```