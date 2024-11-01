### github新建仓库 
- **初始化仓库**
```bash
echo "# Name" >> README.md
git init
git add README.md
git commit -m "first commit" 
git branch -M main
git remote add origin 仓库地址 //本地与远端跟踪
git push -u origin main
```
- **上传文件**
```bash
git clone 仓库地址  //下载仓库至本地
git add . //添加所有文件
git status //查看仓库状态
git commit -m "xxxx"  //提交记录与原因
git push //提交
```


<hr>

## git 基础配置

- 设置 [全局] 提交人
```bash
git config [--global] user.name "Your Name"
```

- 设置 [全局] 提交人的Email地址：
```bash
git config [--global] user.email "email@example.com"
```

- 设置Git使用Socks5代理 http/https 协议：
```bash
git config --global http/https.proxy 
```
    
- 配置用户名和密码的存储方式：

      cache：将登录凭证存放在内存中，默认 15 分钟后清除（可以设置自 定义超时时间）
```bash
git config --global credential.helper cache
```

    自定义超时时间（例如，设置为 1 小时）：
```bash
git config --global credential.helper 'cache --timeout=3600'
```

    store：登陆凭证用明文的形式存放在磁盘中，永不过期
```bash
git config --global credential.helper store
```

    manager：使用 Git Credential Manager，它提供更安全的凭证存储和管理
```bash
git config --global credential.helper manager
```

- 取消 [全局] 配置：
```bash
git config [--global] --unset ConfigName
```

- 查看 [全局] 配置：
```bash
git config [--global] --list
```

<hr>

## git 代理

- 查看当前代理
```bash
git config --global --get http.proxy
git config --global --get https.proxy
```
- 全局设置代理
```bash
// 在仓库的根目录下运行以下命令
git config --global http.proxy http://代理地址:端口
git config --global https.proxy http://代理地址:端口
```
- 为单个仓库设置代理
```bash
git config http.proxy http://代理地址:端口
git config https.proxy http://代理地址:端口
```
- 取消代理
```bash
git config --global --unset http.proxy
git config --global --unset https.proxy
```

<hr>

## git 分支管理

	创建分支
```bash
git branch branchname
```
	合并分支
```bash
git merge
```
	列出分支
```bash
git branch
```
	切换分支
```bash
git checkout branchname
```
	创建并切到此分支
```bash
git checkout -b branchname
```
	删除分支
```bash
git branch -d branchname
```
 
## git 查看历史管理
	查看历史提交记录
```bash
git log
```
	查看历史记录的简洁的版本
```bash
git log --oneline
```
	  查看历史中什么时候出现了分支、合并
```bash
git log --graph
```
	 参数来逆向显示所有日志 
```bash
git log --reverse
```
	查看历史和未来版本
```bash
git reflog
```
	进行已修改或者暂存，但未提交文件退回
```bash
git reset --hard
```
	进行已提交，但是未推送的版本回退
```bash
git rest --hard origin/master
```
	以列表形式查看指定文件的历史修改记录
```bash
git blame <file>
```
	回到上一个版本（进行已提交且推送的回退）
```bash
git reset --hard HEAD^
```
	汇到指定版本 
```bash
git reset --hard <ID>
```
	将暂存区的文件恢复到工作区
```bash
git checkout --<file>
```

<hr>  

## GitHub 上传大文件（>100M）
- 下载Git LFS(Git Large File)客户端  
	官网链接： `https://git-lfs.com/`

- 安装git lfs (一个仓库里面执行一次)
```bash
git lfs install
```

- 要将存储库中的文件类型与 `Git LFS` 相关联， 请输入 `git lfs track`，后跟要自动上传到 `Git LFS` 的文件扩展名的名称。
```bash
git lfs track "*.扩展名"
```
 或者 
 ```bash
 git lfs track "文件名.扩展名"
 ```
 
- 添加.gitattributes（配置文件，缺少它执行执行其他git操作可能会有问题）
```bash
git add .gitattributes
```

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
```bash
git pull //先拉取最新的后，在进行提交
```

- `Github`报错：`OpenSSL SSL_connect: SSL_ERROR_SYSCALL in connection to github.com:443`
  
使用git命令进行 push和pull时，出现以上报错:
  ```bash
   git config --global http.sslBackend "openssl"
  ```

<hr>

**Github文档 `https://docs.github.com/zh`**