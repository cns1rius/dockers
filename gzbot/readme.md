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
- url：靶场url（如果出现错误 请在start.sh中直接修改）

## 文件映射

可将上述文件进行文件映射 方便配置

## qq session

由于鹅厂加强验证 本容器无法完全自动化

需在本容器第一次启动时 进入`app/gzbot`目录下手动执行`go-cqhttp`

会存在请求短信验证码的过程 输入执行成功后 qq session储存在容器中 然后重启容器

`docker restart gzbot`

即可正常运行

若较长时间后出错

- 可按上述步骤重新生成qq session
- 通过`gzbot/logs/xxx.log`
- 通过容器的开放端口调试
  - 5700 ==cqhttp==端口
  - 8080 qsign端口
