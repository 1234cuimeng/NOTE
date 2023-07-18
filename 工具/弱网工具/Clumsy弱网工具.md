# <center> Clumsy 弱网络环境模拟工具使用介绍
## 简介

  利用封装 Winodws Filtering Platform 的WinDivert 库, clumsy 能实时的将系统接收和发出的网络数据包拦截下来，人工的造成延迟，掉包和篡改操作后再进行发送。无论你是要重现网络异常造成的程序错误，还是评估你的应用程序在不良网络状况下的表现，clumsy都能让你在不需要额外添加代码的情况下，在系统层次帮你达到想要的效果

<br>

## 过滤器语法介绍
- outbound：是否为输出数据包

- inbound：是否为输入数据包

- ifldx：网络设备index

- subIfIdx：副网络设备index

- ip：是否为IPv4

- ipv6：是否为Ipv6

- icmp：是否为ICMP

- tcp：是否为TCP

- udp：是否为UDP

- ip.*: IPv4的参数（见DIVERT_IPHDR

- ipv6.*：IPv6的参数(见DIVERT_IPV6DHR

- icmp.*：ICMP的参数(见DIVERT_ICMPHDR

- icmpv6.*：ICMPV6的参数(见DIVERT_ICMPV6HDR

- tcp.*：TCP的参数(见DIVERT_TCPHDR

- tcp.PayloadLength：TCP数据长度

- udp.*：UDP的参数（见DIVERT_UDPHDR

> 可以用“< ==”，“> ==”，“and”, “or”， “=”进行过滤器设置

<br>

## 预设过滤器
  可以将常用个过滤器写到clumsy.exe所在文件夹下的config.txt中
  
<br>

## 功能设置
  勾选左侧的复选框后才可对右与左侧复选框功能对应的参数进行设置。每个功能左边都有一个小圆点图标，其起作用时就会变绿。在数据包捕获开启的情况下，可以实时开启/关闭任何功能，它们都会即时生效。
  
- 延迟(Lag),把数据包缓存一段时间后再发出，这样可以模拟网络延迟的状况

- 掉包(Drop),随机丢弃一些数据

- 节流(Throttle),把一小段时间内的数据拦截下来，并再在之后的统一时间一起发出去

- 乱序(Out of order)，打乱数据包发送的顺序

- 篡改(Tamper),随机修改小部分的数据包内容

> **其中：**
- Lag time设置延迟毫秒数，

- Chance设置该功能发生的概率；

- Inbound/Outboud 设置是否处理输入/输出数据包。这里是filter基础上提供的一个选择的机会，可实时生效

<br>

## 使用方法
**1. 设置过滤器**

**2. 功能设置(可选)**

**3. 点击Start**

**4. 其它测试操作**

**5. 点击Stop**
 
