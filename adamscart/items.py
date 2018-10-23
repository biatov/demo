# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AdamscartItem(scrapy.Item):
    feed_product_type = scrapy.Field()
    item_sku = scrapy.Field()
    brand_name = scrapy.Field()
    external_product_id = scrapy.Field()
    external_product_id_type = scrapy.Field()
    item_name = scrapy.Field()
    manufacturer = scrapy.Field()
    recommended_browse_node = scrapy.Field()
    part_number = scrapy.Field()
    mfg_warranty_description_labor = scrapy.Field()
    standard_price = scrapy.Field()
    quantity = scrapy.Field()
    maximum_retail_price = scrapy.Field()
    main_image_url = scrapy.Field()
    other_image_url1 = scrapy.Field()
    other_image_url2 = scrapy.Field()
    other_image_url3 = scrapy.Field()
    variation_theme = scrapy.Field()
    parent_sku = scrapy.Field()
    relationship_type = scrapy.Field()
    parent_child = scrapy.Field()
    update_delete = scrapy.Field()
    product_description = scrapy.Field()
    model = scrapy.Field()
    bullet_point1 = scrapy.Field()
    bullet_point2 = scrapy.Field()
    bullet_point3 = scrapy.Field()
    bullet_point4 = scrapy.Field()
    bullet_point5 = scrapy.Field()
    generic_keywords1 = scrapy.Field()
    generic_keywords2 = scrapy.Field()
    generic_keywords3 = scrapy.Field()
    generic_keywords4 = scrapy.Field()
    generic_keywords5 = scrapy.Field()
    included_components = scrapy.Field()
