from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector
from CrawlPubComp.items import CrawlpubcompItem

class BloombergBasicSpider(BaseSpider):
    name = "bloomberg_basic"
    allowed_domains = ["http://investing.businessweek.com/"]
    start_urls = (
        'http://investing.businessweek.com/research/common/symbollookup/symbollookup.asp?letterIn=A',
        )

    def parse(self, response):
	hxs = HtmlXPathSelector(response)
	items = []
	company_names = hxs.select('//*[@id="columnLeft"]/table/tbody/tr/td[1]/a/text()').extract()
	country_names = hxs.select('//*[@id="columnLeft"]/table/tbody/tr/td[2]/text()').extract()
	industry_names = hxs.select('//*[@id="columnLeft"]/table/tbody/tr/td[3]/text()').extract()
	for com, count, ind in zip(company_names, country_names, industry_names):
	    items.append(CrawlpubcompItem(company=com, country=count, industry=ind))
        return items[0]
