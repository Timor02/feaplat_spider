# -*- coding: utf-8 -*-
"""
Created on 2022-01-04 18:13:32
---------
@summary:
---------
@author: cao.xiang2
"""

import feapder


class AirSpiderTest(feapder.AirSpider):
    def start_requests(self):
        yield feapder.Request("https://www.baidu.com")

    def parse(self, request, response):
        print(response)


if __name__ == "__main__":
    AirSpiderTest().start()