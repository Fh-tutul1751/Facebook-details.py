import scrapy

class FacebookSpider(scrapy.Spider):
    name = "facebook"
    start_urls = [
        'https://www.facebook.com/profile.php?id={100011474559413}',
    ]

    def parse(self, response):
        # Extract phone numbers and emails
        phone_numbers = response.css('span.phone::text').getall()
        emails = response.css('a.email::text').getall()

        yield {
            'phone_numbers': phone_numbers,
            'emails': emails,
        }
