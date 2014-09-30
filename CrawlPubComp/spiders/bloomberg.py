from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.contrib.spiders import CrawlSpider, Rule
from CrawlPubComp.items import CrawlpubcompItem

class BloombergSpider(CrawlSpider):
    name = 'bloomberg'
    allowed_domains = ['businessweek.com']
    start_urls = ['http://investing.businessweek.com/research/common/symbollookup/symbollookup.asp?letterIn=A']

        #Rule(SgmlLinkExtractor(allow=(r'\?letterIn=B&firstrow=[0-9]*',)), follow = True),
#
    rules = ( 
        Rule(SgmlLinkExtractor(allow=r'symbollookup/symbollookup.asp\?letterIn=A&firstrow=[0-9]'), callback='parse_item', follow = True),
    )

    def parse_item(self, response):
	hxs = HtmlXPathSelector(response)
	items = []
	company_names = hxs.select('//*[@id="columnLeft"]/table/tbody/tr/td[1]/a/text()').extract()
	country_names = hxs.select('//*[@id="columnLeft"]/table/tbody/tr/td[2]/text()').extract()
	industry_names = hxs.select('//*[@id="columnLeft"]/table/tbody/tr/td[3]/text()').extract()
	for com, count, ind in zip(company_names, country_names, industry_names):
	    items.append(CrawlpubcompItem(company=com, country=count, industry=ind))
        #return items[0]
