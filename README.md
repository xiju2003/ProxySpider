# ProxySpider V1.0
基于插件化的多线程代理地址爬虫框架。

## 目录结构
```
ProxySpider         # 主目录
    ├─spiders       # 爬虫脚本
    └─utils         # 核心目录
```
其中爬虫插件全部放在spiders文件夹中。
utils为核心文件，若不进行二次开发，基本不需改动。

## 插件编写规则
见_ExampleSpider.py文件，该文件为插件模板，需要实现的接口在注释中已经给出。

同时可以参考KDLHASpider.py，该文件为一个已经完成的插件，可以爬取某网站提供的当日的HTTP代理。

注意：目前该框架还在开发中，可能会对插件接口进行改动，请多加留意更新。

一个完整的爬虫插件结构如下：
```python
#!/usr/bin/env python
# coding: utf-8

__author__ = "lightless"
__email__ = "root@lightless.me"

class ExampleSpider:    # 文件名与类名相同。因为本文件仅作为示例，所以文件名以下划线开头，在编写自己的插件时请注意，以下划线开头的插件文件是不会被加载进框架的。
    def __init__(self):
        # 待爬取的URL
        self.url = "Your url here."
        # 代理类型，包括HTTP，shadowsocks，VPN
        self.type = "HTTP"
        # 一些你自己的备注，建议填写以作区分
        self.tag = "鲲鹏-全球-高匿代理"
        # Result Queue
        self.result_queue = None

    # 设置结果队列，通常复制该函数即可，不需要修改。
    def set_result_queue(self, result_queue):
        self.result_queue = result_queue

    # 爬取函数，编写自己的爬虫
    def run(self):
        # TODO: Add your process here...
        # TODO: delete these lines below, just an example...
        t = []
        s = {"ip": "11.22.33.44", "port": "8080", "type": u"透明", "protocol": "HTTP", "location": u"Taiwan", "time": "2.6"}
        t.append(s)
        s = {"ip": "22.33.44.55", "port": "3128", "type": u"高匿", "protocol": "HTTPS", "location": u"江苏省南京市 联通", "time": "5"}
        t.append(s)
        tt = [{
            "url": self.url,
            "type": self.type,
        }, t]

        # 将爬取的结果放入结果队列中
        self.result_queue.put(tt)


# 该函数用于框架获取本类，通常直接返回类
def get_spider_class():
    return ExampleSpider
```

## 更新日志
* 2016-6-30 V1.0版本完成，基础框架。

