#!/usr/bin/env python
# coding: utf-8
import os

from bs4 import BeautifulSoup
from selenium import webdriver

__author__ = "lightless"
__email__ = "root@lightless.me"


class KPSpider:
    def __init__(self):
        self.url = "http://www.site-digger.com/html/articles/20110516/proxieslist.html"
        self.tag = "鲲鹏-全球-每日更新"
        self.type = "HTTP"
        self.result_queue = None

    def set_result_queue(self, result_queue):
        self.result_queue = result_queue

    def run(self):

        url = self.url
        phantom_path = os.getcwd() + os.sep + "spiders" + os.sep + "phantomjs.exe"
        driver = webdriver.PhantomJS(executable_path=phantom_path)
        driver.get(url)
        raw_html = driver.execute_script("return document.getElementsByTagName('html')[0].innerHTML")

        soup = BeautifulSoup(raw_html, "html5lib")
        table = soup.find("tbody")
        t_result = []
        for tr in table.find_all("tr"):
            each_item = dict()
            td = tr.find_all("td")
            each_item['ip'] = td[0].get_text().split(";")[1].split(":")[0]
            each_item['port'] = td[0].get_text().split(";")[1].split(":")[1]
            each_item['type'] = td[1].get_text()
            each_item['location'] = td[2].get_text().strip()
            th = tr.find_all("th")
            each_item['time'] = th[0].get_text()
            t_result.append(each_item)
        result = []
        info = dict()
        info['url'] = self.url
        info['type'] = self.type
        info['tag'] = self.tag
        result.append(info)
        result.append(t_result)
        self.result_queue.put(result)


def get_spider_class():
    return KPSpider
