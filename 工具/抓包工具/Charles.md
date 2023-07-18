# <center> Charles

## What is Charles
&ensp;Charles 是在 PC 端常用的网络封包截取工具，在做软件测试/APP开发时，我们为了调试与服务器端的网络通讯协议，常常需要截取网络封包来分析。Charles支持 抓取HTTP和HTTPS协议的网络请求和响应，也可以用于分析第三方应用的通讯协议。

<br> 

## Charles 实现原理
&ensp;Charles 是一个代理服务器。配置好PC或手机网络代理后，Charles就像一个中间人，能够捕获到从客户端发到服务器的请求，以及服务器再传递回客户端时的响应，所以我们打开Charles 能够看到HTTP（HTTPS）请求和响应的详细信息

```
flowchart LR
    客户端:Web,App--> Charles 
    Charles-->客户端:Web,App
    Charles-->服务器
    服务器-->Charles
    
```
## Charles 主界面
![charles主界面.png](/工具/img/Charles主界面.png)

**Charles 主要提供两种查看请求的视图，分别名为 “Structure” 和 “Sequence”**
- Structure 视图将网络请求按访问的域名分类（推荐）
- Sequence 视图将网络请求按访问的时间排序

<br>

## Filter 功能：作用是筛选出指定的请求

- **方法一：可以输入关键字来快速筛选出 URL 中带指定关键字的网络请求**
- **方法二：在 Charles 的菜单栏选择 “Proxy”->”Recording Settings”，然后选择 Include 栏，选择添加一个项目，然后填入需要监控的协议，主机地址，端口号。这样就可以只截取目标网站的封包**

![filter.png](/工具/img/Filter.png)

- **方法三（推荐）：在想过滤的网络请求上右击，选择 “Focus”**
![focus.png](/工具/img/Focus.png)

<br>

## Charles抓包教程
- **PC端**
&ensp;启动 Charles 后，第一次 Charles 会请求你给它设置系统代理的权限。你可以输入登录密码授予 Charles 该权限。你也可以忽略该请求，然后在需要将 Charles 设置成系统代理时，选择菜单中的 “Proxy” -> “Mac OS  Proxy” 来将 Charles 设置成系统代理。如下所示
![设置.png](/工具/img/设置.png)

设置Mac OS  Proxy后，可以再检查Mac的WIFI代理设置。默认情况下网页代理（HTTP）和安全网页代理（HTTPS）选项中网络代理服务器显示为127.0.0.1端口为8888