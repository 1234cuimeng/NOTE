## MYSQL 结构化查询语言
- DDL-数据定义语言 - create / drop / alter
- DMl-数据操作语言 - insert / delete / update
- DCL-数据控制语言 - grant / revoke
  
 ## DDL
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
