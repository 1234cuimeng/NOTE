# <center>vim
## what is vim 
Vim 是从 vi 发展出来的一个文本编辑器。代码补全、编译及错误跳转等方便编程的功能特别丰富

<br>

## vim 的使用
基本上 vi/vim 共分为三种模式，分别是==命令模式==（Command mode），==输入模式==（Insert mode）和==底线命令模式==（Last line mode）。 这三种模式的作用分别是

> 输入`vim` 启动vim，就会进入命令模式
- 命令模式：
   - `i` 切换到输入模式，以输入字符
   - `x` 删除当前光标所在处的字符
   - `:` 切换到底线命令模式，以在最底一行输入命令
   - `G/10G` 光标移到文件末尾/光标移到文件第10行
   - `gg` 光标移到行首
   - `H/J/K/L`光标← ↓ ↑ →
   - `ctrl + y` `ctrl + e` 光标移动一行
   - `ctrl + f` `ctrl + b` 翻页
   - `0/$/w` 光标移动到当前行首/行尾/下一个单词
   - `dd/10dd` 删除光标所在行/从光标所在行删除10行
   - `yy/10yy`复制光标所在行/从光标所在行复制10行
   - `p`粘贴
   - `u`撤销
   - `ctrl + r` 恢复
- 输入模式：
   - 字符按键以及Shift组合，输入字符
   - `ENTER`，回车键，换行
   - `BACK SPACE`，退格键，删除光标前一个字符
   - `DEL`，删除键，删除光标后一个字符
   - 方向键，在文本中移动光标
   - `HOME/END`，移动光标到行首/行尾
   - `Page Up/Page Down`，上/下翻页
   - `Insert`，切换光标为输入/替换模式，光标将变成竖线/下划线
   - `ESC`，退出输入模式，切换到命令模式
 - 底线命令模式：
   - `q` 退出程序
   - `w` 保存文件
   - `set nu/nonu` 显示/不显示行号
   - `set ts=4` 修改制表键的空格键
   - `set ruler/noruler` 显示/不显示光标的位置
   - `syntax on/off` 显示/不显示高量语法
 - 映射快捷键：
   - `map <F2> gg999999dd ` 在命令模式按f2清空内容
   - `inoremap _main if __name__ == "__main __":` 在输入模式输入`'_main'`自动替换成 `if __name__ == "__main __":`
 - 多文件操作：
   - `ls` 底线命令模式查看所有打开文件
   - `b 数字` 指定显示那个文件
   - `vs` 垂直拆分窗口
   - `sp` 水平拆分窗口
   - `ctrl + w` 两次切换窗口
   - `wqa` 全部保存退出
   - `vim -d 文件1 文件2` 打开多文件进行版本比较
 - 别名：
   - alias ll='ls -l'
   - unalias ll 取消别名
- 宏操作：
  - `qa` a是寄存器的名字，录制宏 
  - `q` 结束录制
  - `@a` a是寄存器的名字，播放宏
- 查找替换：
  - `/0` 0为查找内容（命令模式）
  - `1,$s/0/10/cgie` 1第一行$最后一行,把0替换成10，c-confirm确认g-global全局模式i-ignore忽略大小写e-error忽略错误(底线命令模式)
  

- 文件搜索：
  - `grep 正则表达式`
  - `find / -name '*.html'` 根据名字搜索
  - `find / -size +10M` 根据大小搜索
  - `find / -ctime` 创建时间
  - `find / -atime` 最后访问时间
  - `find / -mtime` 最后修改时间
  - `find / -type` 文件类型搜索 d/f/l/s
  
  
  

<br>

## vim 配置文件
-  `vim .vimrc`创建空的`.vimrc`文件，以下为文件内容
```
set nu - 显示行号
syntax on - 显示高亮语法
set ts=4 - 制表键空格4个
set expandtab - 使用制表键设置为空格
set autoindent - 自动缩进
set ruler - 显示光标位置
set nohls -取消查找后的颜色标记 

```

- 配置环境变量 
```
cd ~ : 回到用户主目录
ls -a : 查看隐藏文件,找到.bash_profile文件
vim .bash_profile : 打开此文件
找到path 在后面加 :pyhton3安装地址/bin
source .bash_profile : 激活环境变量文件
python --version : 测试是否安装成功
```

<br>

## 链接
- 硬链接

  `test.py`文件名 拷贝在user/bin路径下名为`haha`文件 ，只是引用，不占用内存空间
```
   ln test.py /user/bin/haha 
```
- 软连接（符号链接）
  
  相当于window系统的创建快捷方式
```
  ln -s user/local/python/bin/python3 /user/bin/python3
  ```

<br>





