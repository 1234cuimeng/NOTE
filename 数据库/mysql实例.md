
## SQL行列转换
行列转换在SQL中是一种常见的操作，通过条件聚合、UNION ALL和动态SQL等方法可以实现灵活的行列转换。根据具体的需求选择合适的方法，有助于提高查询的效率和可读性。
- **行转列（Pivot）**

	**示例数据**：

	假设有一个销售表 `sales`：
	
| Year | Month | Sales |
| ---- | ----- | ----- |
| 2023 | Jan   | 100   |
| 2023 | Feb   | 150   |
| 2023 | Mar   | 200   |
| 2024 | Jan   | 120   |
| 2024 | Feb   | 180   |
| 2024 | Mar   | 220   |

	我们希望将月份作为列，年作为行：

| Year | Jan | Feb | Mar |
| ---- | --- | --- | --- |
| 2023 | 100 | 150 | 200 |
| 2024 | 120 | 180 | 220 |

	在MySQL中，可以使用条件聚合来实现行转列：
```sql
SELECT
    Year,
    MAX(CASE WHEN Month = 'Jan' THEN Sales ELSE 0 END) AS Jan,
    MAX(CASE WHEN Month = 'Feb' THEN Sales ELSE 0 END) AS Feb,
    MAX(CASE WHEN Month = 'Mar' THEN Sales ELSE 0 END) AS Mar
FROM
    sales
GROUP BY
    Year;

```

- **列转行：**
	**示例数据**：

	假设有一个库存表 `inventory`：

| Product | Store1 | Store2 | Store3 |
| ------- | ------ | ------ | ------ |
| Apple   | 50     | 30     | 20     |
| Banana  | 60     | 25     | 30     |

我们希望将库存按商店列出：

| Product | Store  | Stock |
| ------- | ------ | ----- |
| Apple   | Store1 | 50    |
| Apple   | Store2 | 30    |
| Apple   | Store3 | 20    |
| Banana  | Store1 | 60    |
| Banana  | Store2 | 25    |
| Banana  | Store3 | 30    |

	在MySQL中，可以使用UNION ALL来实现列转行：
	
```sql
SELECT Product, 'Store1' AS Store, Store1 AS Stock FROM inventory
UNION ALL
SELECT Product, 'Store2' AS Store, Store2 AS Stock FROM inventory
UNION ALL
SELECT Product, 'Store3' AS Store, Store3 AS Stock FROM inventory;

```

- **动态行列转换**
有时候，列的数量或名称可能是动态的。在这种情况下，可以使用动态SQL。以下是一个动态行转列的示例
```sql
SET @sql = NULL;
SELECT
  GROUP_CONCAT(DISTINCT
    CONCAT(
      'MAX(CASE WHEN Month = ''',
      Month,
      ''' THEN Sales ELSE 0 END) AS `',
      Month, '`'
    )
  ) INTO @sql
FROM sales;

SET @sql = CONCAT('SELECT Year, ', @sql, ' FROM sales GROUP BY Year');

PREPARE stmt FROM @sql;
EXECUTE stmt;
DEALLOCATE PREPARE stmt;
```

## partition

## 查询表中重复的数据

- 特定列的重复数据
```sql
SELECT column_name, COUNT(*)
FROM your_table
GROUP BY column_name
HAVING COUNT(*) > 1;
```
- 多列重复数据
```sql
SELECT column1, column2, COUNT(*)
FROM your_table
GROUP BY column1, column2
HAVING COUNT(*) > 1;
```
- 查找出相对应的重复记录的信息
```sql
SELECT *
FROM your_table
WHERE (column1, column2) IN (
    SELECT column1, column2
    FROM your_table
    GROUP BY column1, column2
    HAVING COUNT(*) > 1
);

```

## 第二高的薪水

给定一个如下定义的数据表，编写查询语句获取并返回 `Employee` 表中第二高的薪水 。如果不存在第二高的薪水，查询应该返回 `null` 。

|字段名|数据类型|
|---|---|
|id|int|
|salary|int|

**示例：**

输入：Employee表

|id|salary|
|---|---|
|1|100|
|2|200|
|3|300|

输出：

| SecondHighestSalary |
| ------------------- |
| 200                 |
**答案**
```
select ifnull(
	select distinct salary
	from Employee
	order by salary Desc
	limit 1 offset 1
)
```
-  `limit N,M` : 相当于`limit M offset N` , 从第 N 条记录开始, 返回 M 条记录
- `IFNULL(..., NULL)`：这个函数确保如果子查询没有返回结果（例如，没有第二高的薪水），它将返回 `NULL`。

## 上升的温度

给定一个如下定义的数据表，编写一个 SQL 查询，来查找与之前（昨天的）日期相比温度更高的所有日期的 `id` 。

|字段名|数据类型|
|---|---|
|id|int|
|recordDate|date|
|temperature|Int|

**示例**

|id|recordDate|temperature|
|---|---|---|
|1|2015-01-01|10|
|2|2015-01-02|25|
|3|2015-01-02|20|
|4|2015-01-04|30|

**输出**

|id|
|---|
|2|
|4|
```sql
SELECT u.id 
FROM Weather u, Weather v
WHERE DATEDIFF(u.recordDate, v.recordDate) = 1 
  AND u.Temperature > v.Temperature;
```
- DATEDIFF() 函数是 SQL Server 中的一个日期函数，用于计算两个日期之间的时间间隔。它接受三个参数：时间间隔单位、开始日期和结束日期，并返回两个日期之间的单位时间间隔。这是语法`DATEDIFF(interval, start_date, end_date)`（interval 参数可以是下列的值：`year`：年`quarter`：季度，`month`：月， `dayofyear`：一年中的第几天，`day`：天 `week`：周，`weekday`：工作日，`hour`：小时，`minute`：分钟，`second`：秒，`millisecond`：毫秒）
- 

## 删除重复的电子邮箱

给定一个如下定义的数据表，编写一个 SQL **删除语句**来 **删除** 所有重复的电子邮件，只保留一个id最小的唯一电子邮件。

|字段名|数据类型|
|---|---|
|id|int|
|email|Archer|

**示例**

| id  | email            |
| --- | ---------------- |
| 1   | john@example.com |
| 2   | bob@example.com  |
| 3   | john@example.com |

**输出**

|id|email|
|---|---|
|1|john@example.com|
|2|bob@example.com|
```sql
delete from person
where id mot in
	select t.id 
	from(select min(id) from person group by email) t
```
还有比较简单的建立双表，直接找到email相同且id较大的数据进行删除
```sql
delete u
from Person u , Person v
where v.id < u.id and u.email = v.email 
```
## 分数排名

给定如下的表格，编写SQL查询对分数进行排序。排名按以下规则计算:

- 分数应按从高到低排列。
- 如果两个分数相等，那么两个分数的排名应该相同。
- 在排名相同的分数后，排名数应该是下一个连续的整数。换句话说，排名之间不应该有空缺的数字。

按 score 降序返回结果表。

|字段名|数据类型|
|---|---|
|id|int|
|score|decimal|

**示例**

|id|score|
|---|---|
|1|3.50|
|2|3.65|
|3|4.00|
|4|3.85|
|5|4.00|
|6|3.65|

**输出**

|Score|Rank|
|---|---|
|4.00|1|
|4.00|1|
|3.85|2|
|3.65|3|
|3.65|3|
|3.50|4|

```sql
select score,dense_rank() over(order by Score desc) as 'rank'
from Scores;
```
- **DENSE_RANK() 窗口函数**：
	`DENSE_RANK() OVER (ORDER BY score DESC) AS 'rank'`：这使用了 `DENSE_RANK()` 窗口函数来对分数进行排名。具体解释如下：
    - `DENSE_RANK()`：这是一个窗口函数，用于为排序中的每个分数生成密集排名。密集排名的特点是相同分数的排名相同，后续排名不会跳过。
    - `OVER (ORDER BY score DESC)`：这个子句指定了排名的排序顺序。`ORDER BY score DESC` 表示按照分数降序排列。

##  患某种疾病的患者
给定如下的数据表，写一条 SQL 语句，查询患有 I 类糖尿病的患者 ID （patient_id）、患者姓名（patient_name）以及其患有的所有疾病代码（conditions）。I 类糖尿病的代码总是包含前缀 DIAB1 。
按任意顺序返回结果表。

|字段名|数据类型|
|---|---|
|patient_id|int|
|patient_name|varchar|
|conditions|varcher|

**示例**

|patient_id|patient_name|conditions|
|---|---|---|
|1|Daniel|YFEV COUGH|
|2|Alice||
|3|Bob|DIAB100 MYOP|
|4|George|ACNE DIAB100|
|5|Alain|DIAB201|

**输出**

|patient_id|patient_name|conditions|
|---|---|---|
|3|Bob|DIAB100 MYOP|
|4|George|ACNE DIAB100|
```sql
select *
from patient
where conditions like 'DIAB%' or conditions like '%DIAB1%'
```