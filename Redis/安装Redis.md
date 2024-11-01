
## linux源码安装Redis
```bash
wget http://download.redis.io/releases/redis-6.0.8.tar.gz
tar xzf redis-6.0.8.tar.gz
cd redis-6.0.8
make
```
- 执行完 make 命令后，redis-6.0.8 的 src 目录下会出现编译后的 redis 服务程序 redis-server，还有用于测试的客户端程序 redis-cli：下面启动 redis 服务：
```bash
 cd src
 ./redis-server
```
## Ubuntu apt 命令安装

- 在 Ubuntu 系统安装 Redis 可以使用以下命令
 `sudo apt update`
 `sudo apt install redis-server`
- 启动 Redis
 `redis-server`
- 查看 redis 是否启动？
 `redis-cli`
- 是否成功安装Redis
 `redis 127.0.0.1:6379> ping`
> 127.0.0.1 是本机 IP ，6379 是 redis 服务端口。现在我们输入 PING 命令。PONG说明安装成功

## 测试Redis安装成功
```bash
redis -server --version
redis -cli --verson
redis -sentinel --version
```
