#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Python application to fetch, store and offline search Reddit data.
Requirements:
1. Python 2.7+
2. requests (pip install requests)
3. elasticsearch (pip install elasticsearch)
4. ElasticSearch server running
(downlaod from https://www.elastic.co/downloads/elasticsearch, install and start)
"""


__author__ = 'Rajendra Kumar Uppal'
__copyright__ = "Copyright 2015, Rajendra Kumar Uppal"
__credits__ = ["Fletcher Heisler", "Rajendra Kumar Uppal"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Rajendra Kumar Uppal"
__email__ = "rajen.iitd@gmail.com"
__status__ = "Production"


import requests
from elasticsearch import Elasticsearch


class Reddit():
    pass


def main():
    es = Elasticsearch()
    
    # get top 100 IAMA posts of all time
    response = requests.get("http://api.reddit.com/r/iama/top/?t=all&limit=1", 
        headers={"User-Agent":"TrackMaven"})
    fields = ['title', 'selftext', 'author', 'score', 'ups', 'downs', 
        'num_comments', 'url', 'created']
    
    # loop through the response and add each data dictionary to reddit index
    for i, iama in enumerate(response.json()['data']['children']):
        content = iama['data']
        doc = {}
        for field in fields:
            doc[field] = content[field]
        print doc
        es.index(index='reddit', doc_type='iama', body=doc)


if __name__ == '__main__':
    main()
