# -*- coding: utf-8 -*-
import scrapy
import re

class RenrenSpider(scrapy.Spider):
    name = 'renren'
    allowed_domains = ['renren.com']
    # 个人中心页网址
    start_urls = ['http://www.renren.com/377276202/profile']

    def start_requests(self):
        # 登录之后用 chrome 的 debug 工具从请求中获取的 cookies
        cookiesstr = "anonymid=kg7n611y-b5mr1w; depovince=ZGQT; jebecookies=5c28f7df-6d60-4d8d-b51c-66d89488317b|||||; _r01_=1; ick_login=f66dac6a-23fa-49ef-961d-4f903f5ab2a5; taihe_bi_sdk_uid=34b0dc2ae0221dc4b7e5c90355795d32; taihe_bi_sdk_session=91f96dc1f229901fe396e8b2648e924d; _de=88E3491E55C4A9E9340E4CEC836F3769696BF75400CE19CC; p=0c9700fb50538e0310832582e8d0d6f32; first_login_flag=1; ln_uact=923686643@qq.com; ln_hurl=http://hdn.xnimg.cn/photos/hdn121/20140208/1140/h_main_oD1r_3e170000b300111a.jpg; t=fb823c3079522096dcb6de78220b91d52; societyguester=fb823c3079522096dcb6de78220b91d52; id=377276202; xnsid=df2590c9; ver=7.0; loginfrom=null; wp_fold=0"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookiesstr.split("; ")}
        print(cookies)
        # 携带 cookies 的 Request 请求
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        # 从个人中心页查找关键词"闲欢"并打印
        # print(response.body.decode())
        print(re.findall("谷世宇", response.body.decode()))
