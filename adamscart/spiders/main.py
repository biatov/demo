import scrapy
import re
import json
from ..items import AdamscartItem


class Main(scrapy.spiders.SitemapSpider):
    name = 'main'
    allowed_domains = ['adamscart.com']

    def __init__(self, *args, **kwargs):
        super(Main, self).__init__(*args, **kwargs)
        self.sitemap_urls = ['https://www.adamscart.com/sitemap_products_1.xml',
                             'https://www.adamscart.com/sitemap_products_2.xml']
        self.sitemap_rules = [('product\/.*', 'parse')]
        self._cbs = list()
        for r, c in self.sitemap_rules:
            if isinstance(c, str):
                c = getattr(self, str(c))
            self._cbs.append((re.compile(r), c))
        self._follow = [re.compile(x) for x in self.sitemap_follow]

    def parse(self, response):
        product_alias = response.url.split('/')[-1]
        product_url = 'https://www.adamscart.com/entity/ms.products?q={"alias":"%s"}' % product_alias
        # category_url = f'https://www.adamscart.com/api/1/entity/ms.products?facetgroup=default_category_facet&facets=true&filters=[{"field":"categories","type":"manual","value":["{category_alias}"],"operator":"in"},{"field":"publish","type":"manual","value":"1"}]&limit=500&sort=&start=0&total=1'
        yield scrapy.Request(
            url=product_url,
            callback=self.parse_product
        )

    def parse_product(self, response):
        json_response = json.loads(response.body_as_unicode())
        item = AdamscartItem()
        product = json_response.get('records', [])
        product = product[0] if product else {}
        item['feed_product_type'] = ', '.join(product.get('collections', []))
        item['item_sku'] = product.get('sku')
        item['brand_name'] = product.get('brand')
        item['external_product_id'] = product.get('_id')
        item['external_product_id_type'] = ''
        item['item_name'] = product.get('name')
        item['manufacturer'] = ''
        item['recommended_browse_node'] = ''
        item['part_number'] = ''
        warranty = list(filter(None, map(lambda p: p if 'Warranty' in p else None, product.get('features', []))))
        warranty = warranty[0].replace('Warranty', '').replace(':', '').strip() if warranty else ''
        item['mfg_warranty_description_labor'] = warranty
        item['standard_price'] = product.get('price')
        item['quantity'] = product.get('inventory_quantity')
        item['maximum_retail_price'] =product.get('compare_price')
        start_image_url = 'https://cdn.storehippo.com/s/58a82124a29a114a6cd3b613'
        images = list(map(lambda i: '%s/%s' % (start_image_url, i.get('image')), product.get('images', [])))
        item['main_image_url'] = images[0] if images else ''
        item['other_image_url1'] = images[1] if len(images) >= 2 else ''
        item['other_image_url2'] = images[2] if len(images) >= 3 else ''
        item['other_image_url3'] = images[3] if len(images) >=4 else ''
        item['variation_theme'] = ''
        item['parent_sku'] = ''
        item['relationship_type'] = ''
        item['parent_child'] = ''
        item['update_delete'] = product.get('updated_on')
        item['product_description'] = re.sub(r'<[^>]*>', '', product.get('description', '')).strip()
        item['model'] = ''
        features = product.get('features', [])
        item['bullet_point1'] = features[0] if features else ''
        item['bullet_point2'] = features[1] if len(features) >= 2 else ''
        item['bullet_point3'] = features[2] if len(features) >= 3 else ''
        item['bullet_point4'] = features[3] if len(features) >= 4 else ''
        item['bullet_point5'] = features[4] if len(features) >= 5 else ''
        item['generic_keywords1'] = ''
        item['generic_keywords2'] = ''
        item['generic_keywords3'] = ''
        item['generic_keywords4'] = ''
        item['generic_keywords5'] = ''
        item['included_components'] = ''
        yield item
