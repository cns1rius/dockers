# GZbot

- 基于qsign镜像进行构建

- 使用`go-cqhttp`作为qq服务应用

- 使用修改后的gzbot.py获取gz信息并发送给go-cqhttp

## 配置方法

### docker env参数

- QQnum：QQ号
- QQpasswd：QQ密码（有些特殊字符需用`\`转义）
- groupNum：通知群号
- gameId：比赛号（例如3）
- url：靶场url

## 文件映射

可将上述文件进行文件映射 方便配置
