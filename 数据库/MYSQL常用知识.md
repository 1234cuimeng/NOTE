## 数据库的三大范式
**数据库的三大范式**是数据库设计中的基础原则，旨在减少数据冗余和提高数据的一致性。它们分别是：

1. **第一范式（1NF）**：确保每个列中的值是原子性的，不可再分的。每个表格中的列都只包含单一类型的值，每个字段不能包含多个值或列表。
**示例**：
```
违反1NF:
学生表：{学生ID, 学生姓名, 课程1, 课程2, 课程3}

满足1NF:
学生课程表：{学生ID, 学生姓名, 课程}

```
2.**第二范式（2NF）**：在满足第一范式的基础上，确保表中的每个非主键列完全依赖于主键，而不是部分依赖。也就是说，非主键列不能依赖于主键的一部分。
**示例**
```
违反2NF:
学生课程表：{学生ID, 课程ID, 课程名称, 教师姓名}

满足2NF:
学生课程表：{学生ID, 课程ID}
课程表：{课程ID, 课程名称, 教师姓名}
```
3.**第三范式（3NF）**：在满足第二范式的基础上，确保表中的每个非主键列都直接依赖于主键，而不是通过其他非主键列间接依赖。这意味着不存在传递依赖
**示例**：
```
违反3NF:
学生课程表：{学生ID, 课程ID, 课程名称, 教师姓名, 教师办公室}

满足3NF:
学生课程表：{学生ID, 课程ID}
课程表：{课程ID, 课程名称, 教师ID}
教师表：{教师ID, 教师姓名, 教师办公室}

```

## 窗口函数
窗口函数（Window Functions）在 SQL 中是一种强大的工具，可以对行集合中的每一行执行计算，同时保留行的细节。窗口函数不会像聚合函数那样对行进行分组并返回一条汇总数据，而是对查询结果的每一行都应用计算，类似于数据表中的“窗口”。

窗口函数的基本语法如下：
```sql
<window_function> OVER (
    [PARTITION BY <partition_expression>]
    [ORDER BY <order_expression>]
    [ROWS or RANGE <frame_clause>]
)
```
- **ROW_NUMBER()**：返回分区内每行的唯一行号。
- **RANK()**：返回分区内每行的排名，相同的值具有相同的排名，排名中间会有空缺。
- **DENSE_RANK()**：类似 RANK()，但排名中间没有空缺
- - **FIRST_VALUE()**：返回窗口内排序后的第一个值。
- **LAST_VALUE()**：返回窗口内排序后的最后一个值。
- **SUM()、AVG()、MIN()、MAX()** 等聚合函数：在窗口内应用这些聚合计算。
### 示例

	假设有一张名为 `sales` 的表，包含如下数据：

| id  | salesperson | region | sales_amount | sales_date |
| --- | ----------- | ------ | ------------ | ---------- |
| 1   | Alice       | North  | 1000         | 2023-01-01 |
| 2   | Bob         | South  | 1500         | 2023-01-02 |
| 3   | Charlie     | North  | 2000         | 2023-01-03 |
| 4   | David       | East   | 2500         | 2023-01-04 |
| 5   | Eve         | West   | 3000         | 2023-01-05 |
| 6   | Frank       | North  | 2000         | 2023-01-06 |
- ROW_NUMBER示例
	为每个区域内的销售人员按销售金额降序排列并分配一个唯一的行号。
```sql
select region, sales_amount, row_number() over (paptition by region order by sales_amoun t desc) as rank
from sales

'''
结果输出
| salesperson | sales_amount | rank |
|-------------|--------------|------|
| Charlie     | 2000         | 1    |
| Frank       | 2000         | 2    |
| Alice       | 1000         | 3    |
| Bob         | 1500         | 1    |
| David       | 2500         | 1    |
| Eve         | 3000         | 1    |

'''
```
- RANK()
	按区域对销售人员的销售额进行排名
```sql
select salesperson, region, sales_amount, rank() over (paptition by region order by sales_amount desc) as rank
from sales
'''
结果输出
| salesperson | region | sales_amount | rank |
|-------------|--------|--------------|------|
| Charlie     | North  | 2000         | 1    |
| Frank       | North  | 2000         | 1    |
| Alice       | North  | 1000         | 3    |
| Bob         | South  | 1500         | 1    |
| David       | East   | 2500         | 1    |
| Eve         | West   | 3000         | 1    |
'''
```
- DENSE_RANK()
	按区域对销售人员的销售额进行排名，销售额相同排名相同，排名相同的分数后，排名数应该是下一个连续的整数。
```sql
select salesperson, region, sales_amount, dense_number() over (paptition by region order by sales_amount desc)
from sales

'''
结果输出
| salesperson | region | sales_amount | rank |
|-------------|--------|--------------|------|
| Charlie     | North  | 2000         | 1    |
| Frank       | North  | 2000         | 1    |
| Alice       | North  | 1000         | 2    |
| Bob         | South  | 1500         | 1    |
| David       | East   | 2500         | 1    |
| Eve         | West   | 3000         | 1    |
'''
```
- LAG() 和 LEAD()
	显示每个销售人员的销售金额，并且显示前一天和后一天的销售金额。
```sql
select 
	salesperson,
	sales_amount, 
	lag(sales_amount, 1) over (order by sales_date) as 
previous_sales,
	lead(sales_amount, 1) over (order by sales_date) as
next_sales
from sales

'''
结果输出
| salesperson | sales_amount | previous_sales | next_sales |
|-------------|--------------|----------------|------------|
| Alice       | 1000         | NULL           | 1500       |
| Bob         | 1500         | 1000           | 2000       |
| Charlie     | 2000         | 1500           | 2500       |
| David       | 2500         | 2000           | 3000       |
| Eve         | 3000         | 2500           | 2000       |
| Frank       | 2000         | 3000           | NULL       |
```

