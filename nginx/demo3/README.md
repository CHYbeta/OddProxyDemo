# README

```
./start.sh

# 关闭
docker-compose rm -fs
```

访问 Weblogic 控制台，触发策略，403

![](static/1.jpg)

利用路径参数进行绕过，访问到控制台
![](static/2.jpg)

具体分析见 [Nginx 场景绕过之三: 斜杠(trailing slash) 与 ;（Weblogic为例）]()