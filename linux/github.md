### 新建仓库 
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
