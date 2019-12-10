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

    def offer(self, offer_id, **params):
        resource = "offer/_id/{0}".format(offer_id)
        return self.get(resource, **params)

    def search(self, keyword, **params):
        resource = "offer/_search"
        params.add({'keyword' : keyword})
        return self.get(resource, **params)