import scrapy


class NewsSpider(scrapy.Spider):
	
	name = 'news'
	#allowed_domains = ['www.sberbank.ru/ru/s_m_business/news'] фильтрует запрос, если не закомментить
	start_urls = ['https://www.sberbank.ru/ru/press_center/all']

	def parse(self, response):
		
		for news in response.css('a.na-article'):
			yield {
				'date': news.css('span.na-article__date::text').get(),
				'text': news.css('span.na-article__title::text').get()
			}
			
		next_page = response.css(
			'div.na-paging a.na-paging__page na-paging__page_next::attr(href)'
		).get()
		print()
		print(next_page)
		print()
		if next_page is not None:
			yield response.follow(next_page, callback=self.parse)
		
			
