Android Studio官网下载 :`[https://developer.android.com/studio?hl=zh-cn](https://developer.android.com/studio?hl=zh-cn)`
JDK下载官网：`[https://www.oracle.com/java/technologies/downloads/#jdk23-mac]`
<h1><center>Windows </center></h1>

## 手机配置
在设置中打开允许开发者模式
## Android Studio sdk存放位置
新建一个工程后，查看sdk地址：Tools → SDK Manager
## 配置adb系统变量
**新建系统变量:在sdk地址后面找到platform-tools，复制此地址，粘到变量值处；变量名：Android_sdk**
![系统变量.png](/工具/img/系统变量.png)

**配置path变量：在系统变量中找到path，编辑-> 新建-> %Android_sdk%**
![path变量.png](/工具/img/path变量.png)

## 测试adb配置是否成功
**在终端输入adb，出现以下表示配置成功**
![adb.png](/工具/img/adb.png)

<br>

## 下载USB driver
**Tools → SDK Manager → SDK Tools，选择 Google USBDriver**
![usb driver.png](/工具/img/usb%20driver.png)


## 下载手机安卓版本对应的平台
**Tools → SDK Manager → SDK Platforms，选择安卓手机对应的安卓系统版本进行下载安装。**
![image](/工具/img/sdk_platforms.png)

## 配置USB driver
**点击电脑→管理→设备管理器→便携设备，选择你的手机，右键选择更新驱动程序，选择浏览我的计算机以查找驱动程序软件。**
![image](/工具/img/企业微信截图_1675399379949.png)
![image](/工具/img/企业微信截图_16753986335790.png)
**在sdk存放的位置下找到以下路径：复制此地址**
![image](/工具/img/企业微信截图_16753990666479.png)
**粘贴到此处**
![image](/工具/img/企业微信截图_16753986811038.png)

<hr>

<h1><center>Mac </center></h1>

`Mac`在下载客户端时，有两种选择：`Mac with Intel Chip` 、 `Mac with Apple Chip`
**如何判断下载哪一种：**

- 点击屏幕左上角`Apple`标志，单机关于本机，如下图所示
    
- 判断**Mac芯片类型**: 显式为 `Inter`， 则表示 `Mac with Intel Chip` ,反之是`Mac with Apple Chip`。
![image](/工具/img/Mac系统.png)

 
## JDK下载

- 如果是`M`系列芯片的选择 `Arm 64 DMG installer`，是`intel`系列的选择 `X64 DMG installer`
    
- 下载完成后双击进行安装，跟着提示依次点击下一步即可完成安装
    
- 安装完成后我们测试一下是否正确完成安装：打开终端`terminal`，输入：`java -version`，显示以下信息表示安装完成。
![image](/工具/img/java_version.png)
- **查询安装路径**：在终端`terminal`输入命令：`/usr/libexec/java_home -V` ，下图是对应版本的安装路径。此路径复制，后面用到。
![image](/工具/img/java_home.png)

## 配置环境变量
打开此文件命令：`open ～/.bash_profile`，在此文件中添加以下：
```Bash
JAVA_HOME=这里是上面复制JDK的安装路径
PATH=$JAVA_HOME/bin:$PATH:.
CLASSPATH=$JAVA_HOME/lib/tools.jar:$JAVA_HOME/lib/dt.jar:.
export JAVA_HOME
export PATH
export CLASSPATH
```

