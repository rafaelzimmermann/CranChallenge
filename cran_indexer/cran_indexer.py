import elasticsearch
from datetime import datetime

class CranIndexer(object):

    INDEXED_FIELDS = ["Package", "Version"]

    def __init__(self):
        self.es = elasticsearch.Elasticsearch("http://localhost:9200/")


    def index(self, package_description):
        remove = []
        for key in package_description:
            if key not in self.INDEXED_FIELDS:
                remove.append(key)
        for key in remove:
            package_description.pop(key, None)

        id = package_description["Package"] + "|" + package_description["Version"]
        package_description['timestamp'] = datetime.now()

        res = self.es.index(index="package", doc_type="description", id=id, body=package_description)

        return res

    def get(self):
        res = self.es.search(index="package", body={"query": {"match_all": {}}})
        print ">>", res
        print("Got %d Hits:" % res['hits']['total'])

        return res['hits']
