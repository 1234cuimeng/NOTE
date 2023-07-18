# <center>Android Studio连接真机


## 手机配置
- 允许开发者模式

<br>

## Android Studio sdk存放位置
新建一个工程后，查看sdk地址：Tools → SDK Manager
## 配置adb系统变量
- ==新建系统变量:在sdk地址后面找到platform-tools，复制此地址，粘到变量值处；变量名：Android_sdk==
![系统变量.png](/工具/img/系统变量.png)
- ==配置path变量：在系统变量中找到path，编辑-> 新建-> %Android_sdk%
![path变量.png](/工具/img/path变量.png)

## 测试adb配置是否成功
==在终端输入-adb，出现以下表示配置成功==
![adb.png](/工具/img/adb.png)

<br>

## 下载USB driver
==Tools → SDK Manager → SDK Tools，选择 Google USBDriver==
![usb driver.png](/工具/img/usb%20driver.png)


## 下载手机安卓版本对应的平台
==Tools → SDK Manager → SDK Platforms，选择安卓手机对应的安卓系统版本进行下载安装。==
![image](/工具/img/sdk_platforms.png)

## 配置USB driver
==点击电脑→管理→设备管理器→便携设备，选择你的手机，右键选择更新驱动程序，选择浏览我的计算机以查找驱动程序软件。==
![image](/工具/img/企业微信截图_1675399379949.png)
![image](/工具/img/企业微信截图_16753986335790.png)
-==在sdk存放的位置下找到以下路径：复制此地址==
![image](/工具/img/企业微信截图_16753990666479.png)
==-粘贴到此处==
![image](/工具/img/企业微信截图_16753986811038.png)
