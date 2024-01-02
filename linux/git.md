### github新建仓库 
- 初始化仓库
`echo "# Name" >> README.md`
`git init`
`git add README.md`
`git commit -m "first commit"` 
`git branch -M main`
`git remote add origin 仓库地址` ==本地与远端跟踪==
`git push -u origin main`

- 上传文件
`git clone 仓库地址`==下载仓库至本地==
`git add .`==添加所有文件==
`git status`==查看仓库状态==
`git commit -m "xxxx"` ==提交记录与原因==
`git push`==提交==

<br>

### 问题解决
- git读取中文文件名

配置.gitconfig 添加以下内容至末尾，.gitconfig文件位置通常在C:\Users\Administrator目录下
```
[gui]  
    encoding = utf-8  
    # 代码库统一使用utf-8  
[i18n]  
    commitencoding = utf-8  
    # log编码  
[svn]  
    pathnameencoding = utf-8  
    # 支持中文路径  
[core]
    quotepath = false 
    # status引用路径不再是八进制（反过来说就是允许显示中文了
```
- 远端与本地不同步时
   
`git pull`==先拉取最新的后，在进行提交

## git 基础配置
- 设置 [全局] 提交人：
      $ git config [--global] user.name "Your Name"

- 设置 [全局] 提交人的Email地址：
      $ git config [--global] user.email "email@example.com"

- 设置Git使用Socks5代理 http/https 协议：
      $ git config --global http/https.proxy http/https://127.0.0.1:1080

- 配置用户名和密码的存储方式：
cache：登陆凭证存放在内存中，15分钟后清楚
store：登陆凭证用明文的形式存放在磁盘中，永不过期
manager：关于 manager 的更多信息请参阅 这里
      $ git config --global credential.helper store/cache/manager

- 取消 [全局] 配置：
      $ git config [--global] --unset ConfigName

- 查看 [全局] 配置：
      $ git config [--global] --list

## git 分支管理
`git branch (branchname)` 创建分支
`git checkout (branchname)` 切换分支
`git merge` 合并分支
`git branch` 列出分支
`git checkout -b (branchname)` 创建并切到此分支
`git branch -d (branchname)` 删除分支

## git 查看历史管理
`git log` 查看历史提交记录
 - `--oneline` 查看历史记录的简洁的版本
 - `--graph`查看历史中什么时候出现了分支、合并
 - `--reverse` 参数来逆向显示所有日志
`git reflog` 查看历史和未来版本
`git reset --hard` 进行已修改或者暂存，但未提交文件退回
`git rest --hard origin/master`进行已提交，但是未推送的版本回退
`git blame <file>` 以列表形式查看指定文件的历史修改记录
`git reset --hard HEAD^` 回到上一个版本（进行已提交且推送的回退）
`git reset --hard <ID>` 汇到指定版本 
`git checkout --<file>`  将暂存区的文件恢复到工作区