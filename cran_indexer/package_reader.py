#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
import yaml

class PackageReader(object):
    DESCRIPTION_FILE = "/tmp/descriptions"

    def download(self, path):
        response =  urllib2.urlopen(path)
        return response.read()

    def read_description(self, description):
        return yaml.load(description)

    def read(self, path):
        descriptions_file = self.download(path)
        descriptions = []
        for description in descriptions_file.split("\n\n"):
            descriptions.append(self.read_description(description))
        print len(descriptions)
        return descriptions
