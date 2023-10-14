# GZbot

- 基于qsign镜像进行构建

- 使用`go-cqhttp`作为qq服务应用

- 使用修改后的gzbot.py获取gz信息并发送给go-cqhttp

## 配置方法

### docker env

- QQ号：QQnum
- QQ密码：QQpasswd（有些特殊字符需用`\`转义）
- 通知群号groupNum
- 比赛号（例如3）：gameId

### start.sh

python3 gzbot --url="靶场url" ………………

## 文件映射

可将上述文件进行文件映射 方便配置
