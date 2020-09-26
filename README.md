# ipInfo.icu 服务

基于腾讯云云函数（Serverless Cloud Function，SCF）创建

目的为实践云函数开发流程

目前提供以下 api，更多 api 建造中

ip 查询

`curl ipinfo.icu`

`curl ipinfo.icu/ip`

User-Agent 查询

`curl ipinfo.icu/ua`

或浏览器访问: `ipinfo.icu/ua`

# 步骤

## 建立云函数

云函数 SCF -> 创建云函数 -> Python3.6 环境 -> 上传 ipinfo_app/src/index.py 的代码

## 建立并发布 API 网关

API 网关 -> 服务 -> 新建 -> 管理 API -> 新建 API

分别创建路径为 `/ip` `/ua` `/` 的 3 个 api

后端类型选择 `cloud function` ，选中对应云函数

回到 API 网关服务页面，发布 API 网关服务

## 域名绑定

进入 API 服务页面 -> 自定义域名

新建域名绑定，可看到提示

```
请确认需绑定的域名已经完成解析配置，指向此服务的二级域名。

公网二级域名: service-agaxujsc-************.hk.apigw.tencentcs.com
```

进入 DNS 管理，给域名新建一个 CNAME 记录，回到自定义域名页面，进行绑定

选择 API 服务，协议，自定义路径映射为`/`，环境为`发布`

提交保存即可生效
