# -*- coding: utf-8 -*-
import requests

class Lomadee():
    sandbox_url = "http://sandbox-api.lomadee.com/{0}/{1}/{2}"
    production_url = "https://api.lomadee.com/{0}/{1}/{2}"

    def __init__(self, app_token, source_id, sandbox=False, version='v3'):
        self.app_token = app_token
        self.source_id = source_id
        self.sandbox = sandbox
        self.version = version

    def get_url(self, resource):
        if self.sandbox:
            return self.sandbox_url.format(self.version, self.app_token, resource)
        return self.production_url.format(self.version, self.app_token, resource)

    def get_params(self, **params):
        params.update({'sourceId' : self.source_id })
        return params

    def get(self, resource, **params):
        return requests.get(
            self.get_url(resource),
            params=self.get_params(**params)
        ).json()


class Offers(Lomadee):
    
    def category(self, category_id, **params):
        resource = "offer/_category/{0}".format(category_id)
        return self.get(resource=resource, **params)

    def store(self, store_id, **params):
        resource = "offer/_store/{0}".format(store_id)
        return self.get(resource, **params)

    def offer(self, store_id, offer_id, **params):
        resource = "offer/_id/{0}".format(offer_id)
        params.update({'storeId' : store_id})
        return self.get(resource, **params)

    def search(self, keyword, **params):
        resource = "offer/_search"
        params.update({'keyword' : keyword})
        return self.get(resource, **params)

class Categories(Lomadee):
    
    def all(self, **params):
        resource = "category/_all"
        return self.get(resource, **params)

    def category(self, category_id, **params):
        resource = "category/_id/{0}".format(category_id)
        return self.get(resource, **params)

    def search(self, keyword, **params):
        resource = "category/_search"
        params.update({'keyword' : keyword})
        return self.get(resource, **params)


class Stores(Lomadee):

    def all(self, **params):
        resource = "store/_all"
        return self.get(resource, **params)


class Coupons(Lomadee):

    def all(self, **params):
        resource = "coupon/_all"
        return self.get(resource, **params)

    def coupon(self, coupon_id, **params):
        resource = "coupon/_id/{0}".format(coupon_id)
        return self.get(resource, **params)

    def categories(self, **params):
        resource = "coupon/_categories"
        return self.get(resource, **params)
    
    def stores(self, **params):
        resource = "coupon/_stores"
        return self.get(resource, **params)


class DeepLink(Lomadee):

    def create(self, url, **params):
        resource = "deeplink/_create"
        params.update({'url' : url})
        return self.get(resource, **params)