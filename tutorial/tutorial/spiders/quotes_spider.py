import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"

    start_urls = [
        'http://data-service.golaxy.cn:8080/wde_web/consumption/queryFile?channel=%25E6%2596%25B0%25E9%2597%25BB&endTime=2020-08-04T23:59:59.999Z&startTime=2020-08-03T23:59:59.999Z'
    ]

    def start_requests(self):
        """
        根据cookies模拟登陆人人网，注意settings.py文件的cookies必须是开启的
        :return:
        """
        cookies="JSESSIONID=9F04F138D01A5A1B6E3055055A0C5521; UM_distinctid=17181e5303f15c-001fd3cd78625a-5313f6f-1fa400-17181e53040bb5; JSESSIONID=AE92D3D200FB4959CEB193A5B1A03589"
        cookies = {i.split("=")[0]:i.split("=")[1] for i in cookies.split("; ")}
        yield scrapy.Request(
            self.start_urls[0],
            callback=self.parse,
            cookies=cookies
        )

    def parse(self, response):
        print(response.body)
