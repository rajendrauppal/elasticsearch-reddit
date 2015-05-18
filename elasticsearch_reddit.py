#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Python application to fetch, store and offline search Reddit data.
"""


__author__ = 'Rajendra Kumar Uppal'


import requests
from elasticsearch import Elasticsearch


def main():
    es = Elasticsearch()
    
    # get top 100 IAMA posts of all time
    response = requests.get("http://api.reddit.com/r/iama/top/?t=all&limit=1", headers={"User-Agent":"TrackMaven"})
    fields = ['title', 'selftext', 'author', 'score', 'ups', 'downs', 'num_comments', 'url', 'created']
    
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
