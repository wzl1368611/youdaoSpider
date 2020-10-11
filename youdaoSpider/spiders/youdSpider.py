# -*- coding: utf-8 -*-
import scrapy
import random


# http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
class YoudspiderSpider(scrapy.Spider):
    name = 'youdSpider'
    allowed_domains = ['fanyi.youdao.com']

    # start_urls = ['http://youdao.com/']
    def start_requests(self):
        url = "http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule"
        # http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
        # str="南昌"
        # a=str.encode()
        userAgents = ["Mozilla/5.0 (Macintosh; \
        U; Intel Mac OS X 10_6_8; en-us)\
        AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                      "Mozilla/5.0 (Windows; U; Windows NT 6.1; en-us)\
        AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
                      "Mozilla/5.0 (Macintosh; Intel Mac\
        OS X 10.6; rv:2.0.1) Gecko/20100101 Firefox/4.0.1",
                      "Mozilla/4.0 (compatible; MSIE 7.0; \
        Windows NT 5.1; TencentTraveler 4.0)",
                      "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_3 like\
         Mac OS X; en-us) AppleWebKit/533.17.9 (KHTML, like\
          Gecko) Version/5.0.2 Mobile/8J2 Safari/6533.18.5",

                      ]
        strr = "长城"
        aa = strr.encode()
        userAgent = random.choice(userAgents)
        headers = {
            "user-agent": userAgent,
            "Accept": "application/json, text/javascript, */*; q=0.01",
        }
        yield scrapy.FormRequest(

            url=url,
            headers=headers,
            # 像队列中加入一个表单信息的post请求
            formdata={
                "action": "FY_BY_REALTlME",
                "bv": "0930ba55ca8c5e4b94b06e3db8ae8b55",
                "client": "fanyideskweb",
                "doctype": "json",
                "from": "AUTO",
                "i": aa,
                "keyfrom": "fanyi.web",
                "salt": "15920382269479",
                "sign": "1f678e17a410689cbf780c2ce451ccd7",
                "smartresult": "dict",
                "to": "AUTO",
                "ts": "1592038226947",
                "version": "2.1"

            },
            callback=self.parse
        )

    def parse(self, response):
        print("========================================")
        print(response.body)
