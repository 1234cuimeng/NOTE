```python
!head data/sales_data.csv
```
**说明：**
这个命令是在尝试查看名为 "sales_data.csv" 的文件的开头。通常情况下，`!head` 命令后跟着的部分通常是文件的路径，用来指定查看文件的前几行内容。


```python
sales = pd.read_csv(
    'data/sales_data.csv',
    parse_dates=['Date'])
```
**说明：**
- `pd.read_csv`: 这是 Pandas 库中的一个函数，用于从 CSV 文件中读取数据并创建一个 DataFrame 对象。
- `'data/sales_data.csv'`: 这是要读取的 CSV 文件的路径。前面的 `'data/'` 表示该文件位于名为 "data" 的文件夹中，`'sales_data.csv'` 则是文件的名称。
- `parse_dates=['Date']`: 这个参数告诉 Pandas 库将指定列（在这里是 "Date" 列）中的数据解析为日期时间对象。这在分析时间序列数据时非常有用，因为它使得可以轻松地按日期和时间进行过滤和分析。
- `parse_dates` 参数的值可以是列名的字符串或整数，也可以是列名的列表或整数列表。如果值为整数，表示该列是数据中的第几列；如果是字符串，则表示该列的列名


```python
sales.head()
```
**说明：**
调用`head()`方法来显示前五行数据，以便快速浏览数据的结构和内容


```python
sales.shape
```
**说明：**
- `sales.shape` 是一个属性，用于返回 DataFrame 的维度。具体来说，它会返回一个包含两个元素的元组 `(number_of_rows, number_of_columns)`，分别表示 DataFrame 的行数和列数。
- 例如，如果 `sales` DataFrame 有 100 行和 5 列，那么 `sales.shape` 会返回 `(100, 5)`。
这在数据分析中很有用，因为你可以快速了解数据集的大小和结构。


```python
sales.info()
```
**说明：**
`sales.info()` 是 Pandas DataFrame 对象的方法，用于显示有关 DataFrame 的简要摘要信息。调用 `sales.info()` 可以帮助你了解数据集的整体结构和一些基本统计信息。它会输出以下内容：
- 索引范围：显示 DataFrame 的行索引范围。
-  列的信息：包括每列的名称、非空值的数量、数据类型（如整数、浮点数、对象（字符串）、日期时间等）。
-  内存使用情况：显示 DataFrame 占用的内存大小。


```python
sales.describe()
'''
输出示例：
           Sales      Profit
count  100.000000  100.000000
mean    50.512345    5.678910
std     25.123456    3.456789
min      1.000000    0.123456
25%     25.000000    2.345678
50%     50.000000    5.000000
75%     75.000000    8.345678
max    100.000000   10.000000
# 这个输出提供了关于 `Sales` 和 `Profit` 列的统计信息
'''
```
**说明：**
`sales.describe()` 是 Pandas DataFrame 对象的方法，用于生成描述性统计信息的汇总表。这些统计信息通常包括数值型数据的计数、平均值、标准差、最小值、四分位数以及最大值。默认情况下，`describe()` 只会针对数值型数据生成统计信息。
当你调用 `sales.describe()` 时，它会输出一个包含以下统计信息的 DataFrame：

- count: 非空值的数量。
- mean: 平均值。
- std: 标准差。
- min: 最小值。
- 25%: 第一个四分位数（25th 百分位数）。
- 50%: 中位数（50th 百分位数）。
- 75%: 第三个四分位数（75th 百分位数）。
- max: 最大值。


```python
sales['Unit_Cost'].mean()
```
**说明：**
`sales['Unit_Cost'].mean()`是用于计算 `Unit_Cost` 列的平均值（均值）的 Pandas 方法。平均值是所有数值的总和除以数值的数量，表示数据集的中心位置。


```python
sale['Unit_cost'].median()
```
**说明：**
`sales['Unit_Cost'].median()` 是用于计算 `Unit_Cost` 列的中位数的 Pandas 方法。中位数是将所有数值按大小排序后，位于中间的那个数值。如果数值的个数是偶数，中位数是中间两个数值的平均值。常用它来描述这组数据的集中趋势。


```python
import matplotlib.pyplot as plt
sales['Unit_Cost'].plot(kind='box', vert=False, figsize=(14,6))
```
[[图|箱形图]]
**说明：**
- `sales['Unit_Cost']`：选择 `sales` DataFrame 中的 `Unit_Cost` 列。
- `plot`：这是 Pandas 中的一个方法，用于绘制各种类型的图表。
-  `kind='box'`: 指定要绘制的图标类型为箱形图
- `vert=False`: 将箱形图设置为水平显示（默认是垂直显示）
- `figsize=(14, 6)`: 设置图表的大小，宽度为14，高度为6

