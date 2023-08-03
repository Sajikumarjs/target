import json
from pathlib import Path

import scrapy
import pprint
import w3lib.html


class TargetSpider(scrapy.Spider):
    name = "target"
    product_base_url = ("https://redsky.target.com/redsky_aggregations/v1/web/pdp_client_v1?"
                        "key=9f36aeafbe60771e321a7cc95a78140772ab3e96&tcin={}&is_bot=false&store_id=2303&"
                        "pricing_store_id=2303&has_pricing_store_id=true&has_financing_options=true&"
                        "visitor_id=0189BA22B939020192E6CFF77DAE4159&has_size_context=true&"
                        "latitude=10.200&longitude=76.240&zip=68359&state=KL&skip_personalized=true&"
                        "channel=WEB&page=%2Fp%2Fundefined")
    currency_list = {
        "$": "USD",
        "₹": "INR"
    }

    def __init__(self, *args, **kwargs):
        super(TargetSpider, self).__init__(*args, **kwargs)
        self.url = kwargs.get('url')

    def start_requests(self):
        product_id = self.url.split("/A-")[-1]
        product_url = self.product_base_url.format(product_id)
        yield scrapy.Request(url=product_url, callback=self.parse)

    def parse(self, response):
        product_json = response.json()['data'].get("product")
        if product_json.get('children'):
            for product_item in product_json['children']:
                product = self.get_product(product_item)
                pprint.pprint(product)
        else:
            product = self.get_product(product_json)
            pprint.pprint(product)

    def get_product(self, product_json):
        product = {
            "url": product_json['item']['enrichment']['buy_url'],
            "tcin": product_json['tcin'],
            "upc": product_json['item'].get('primary_barcode'),
            "price_amount": product_json['price'].get('current_retail'),
            "currency": self.currency_list.get(product_json['price']['formatted_current_price'][:1]),
            "description": product_json['item']['product_description'].get('downstream_description'),
            "specs": None,
            "ingredients": [],
            "bullets": "\n".join(product_json['item']['product_description']['soft_bullets']['bullets']),
            "features": [w3lib.html.remove_tags(item) for item in
                         product_json['item']['product_description']['bullet_descriptions']]
        }
        return product