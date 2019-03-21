# -*- coding: utf-8 -*-
from __future__ import (print_function, unicode_literals, division, absolute_import)
import requests
import json

class Request():
    def __init__(self, project, token, package, block, params, base_endpoint):
        self.project = project
        self.token = token
        self.package = package
        self.block = block
        self.params = params
        self.base_endpoint = base_endpoint

    @property
    def urlBuilder(self):
        return self.base_endpoint + self.package + "/" + self.block

    @property
    def call(self):
        response = requests.post(self.urlBuilder,
                                 auth=(self.project, self.token),
                                 headers={'user-agent': 'RapidAPIConnect_Python'},
                                 data=self.params).text

        objectResponse = json.loads(response)

        if 'payload' in objectResponse:
            return objectResponse['payload']
        else:
            return objectResponse
