# -*- coding: utf-8 -*-
import requests

class Lomadee():
    sandbox_url = "http://sandbox-api.lomadee.com/v3/{0}/{1}"
    production_url = "https://api.lomadee.com/v3/{0}/{1}"

    def __init__(self, app_token, source_id, sandbox=False):
        self.app_token = app_token
        self.source_id = source_id
        self.sandbox = sandbox

    def get_url(self, resource):
        if self.sandbox:
            return self.sandbox_url.format(self.app_token, resource)
        return self.production_url.format(self.app_token, resource)

    def get_params(self, **params):
        params.update({'sourceId' : self.sourceId })
        return params

    def get(self, resource, **params):
        return requests.get(
            self.get_url(resource),
            params=self.get_params
        ).json()