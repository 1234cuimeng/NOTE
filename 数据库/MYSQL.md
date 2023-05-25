## MYSQL 结构化查询语言
- DDL-数据定义语言 - create / drop / alter
- DMl-数据操作语言 - insert / delete / update
- DCL-数据控制语言 - grant / revoke
  
 ## CRUD操作
- 创建数据库,默认字符集utf8
 `create database database_name default charset utf8`
- 切换数据库
 `use database_name`
- 删除数据库 
 `drop database database_name` 
- 创建表：定义列，定义类型，约束，主键
 ```
create table tablename
(
column_name1 int not null comment ' XXXX',
column_name2 varchar(20) not null,
column_name3 bit default 1,
column_name4 date,
primary key (column_name1)
);
 ```
 >说明:
 `column_name1`列 int类型，不能为空；comment为注释
 `column_name2`列 varchar类型，最大长度为20；
 `column_name3`列 bit类型，默认值为1；
 `column_name4`列 date类型 ；
 `column_name1`列 为主键
- 删表
 `drop table if exists table_name`
- 修改表
  - 增加列
  `alter table table_name add column column_name varchar(20) `
  - 修改列
  `alter table table_name change column column_name column_name1 varchar(50)`
  - 删除列
  `alter table table_name drop column column_name`
  - 插入数据  
  `insert into table_name values(xxx,xxx,xxx)`
  `insert into table_nam (column1,column2) values(xxx,xxx)`
  - 删除数据
  `delete from table_name where column=xxx `
  - 更新数据
  `update table_name set column3='xxx' where column1=xxx or column1=xxx`

- 添加外键约束
  `alter table table_name add constraint column_name foreign key (colum_name2) references table_name1 (colum_name2)`
  >说明：举例，学生表与学院表，每个学生对应一个学院，每个学院对应多个学生。需要我们将两表进行关联，添加外键约束。可将学院表的编号，作为学生表的外键约束。
  >翻译：在`table_name`表中添加外键约束，名为`column_name` 外键约束是`colum_name2` ，来源于`table_name1`表的主键`colum_name2`

- 添加唯一性约束
  ``


## 查询
- 查所有信息
  `select * from 表名`
- 投影
  `select 列名，列名 from 表名`
- 别名
  `select 列名1 as 别名, 列名2 as 别名 from 表名`
- 筛选
  `select 列名 as 别名，case 列名 when <条件> then '' else '' end as 别名 from 表名`
  `select 列名, 列名 from 表名 where <条件>`
  - `between  and`两者之间
  - `distinct`去重  
  - `is not null` `is null`判断空值
  - `order by`排序(默认升序 asc升序 desc降序)