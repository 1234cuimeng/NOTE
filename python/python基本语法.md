# <center> python基本语法
<hr>
## 注释
- 单行注释：可以使用#
- 多行注释：多个# 或 ''' 和 """
``` python 
'''
这是一个注释多行注释1
'''
"""
这是一个注释多行注释2
"""
# 单行注释

```

<hr>

## 行与缩进

python使用缩进来表示块，使用Tab键或手敲4个空格

<hr>

## 多行语句

如果语句很长，可以使用反斜杠\来实现多行语句

```python 
name = "cuimeng" + "wupong" + \
        "queban" + "heitan" + \
        "fantong"
```

<hr>

## import 与 from...import

在 python 用 import 或者 from...import 来导入相应的模块。
- 将整个模块(somemodule)导入，格式为： **import somemodule**
- 从某个模块中导入某个函数,格式为： **from somemodule import somefunction**
- 从某个模块中导入多个函数,格式为： **from somemodule import firstfunc, secondfunc, thirdfunc**
- 将某个模块中的全部函数导入，格式为：<b> from somemodule import * </b>