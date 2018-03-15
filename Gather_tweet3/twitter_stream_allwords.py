# -*- coding: utf-8 -*-
# easy_install python_twitter
import twitter
import sys
import codecs
from twitter_db import *
import csv


# easy_install の最新版でGetStreamFilterがなければ下記のコード追加
# https://github.com/bear/python-twitter/blob/master/twitter/api.py
def GetStreamFilter(api):

    url = '%s/statuses/filter.json' % api.stream_url
    data = {}

    data['track'] = '#Election2016'
    #data['filter_level'] = 'low'
    #data['locations'] = '-140,-90,150,90'
    #print data

    json = api._RequestStream(url, 'POST', data=data)
    for line in json.iter_lines():
        if line:
            data = api._ParseAndCheckTwitter(line)
            yield data


def main(argvs, argc):
    if argc != 1:
        print ("Usage #python %s" % argvs[0])
        return 1
    # secondary keys
    
    db.create_tables([Twitte], True)

    api = twitter.Api(base_url="https://api.twitter.com/1.1",
                      consumer_key=consumer_key,
                      consumer_secret=consumer_secret,
                      access_token_key=access_token_key,
                      access_token_secret=access_token_secret)

    counter = 1

    for item in GetStreamFilter(api):
        #print (item['id_str'])
        #print (item['text'])
        #if (item['coordinates'] != None):
        #    print (item['coordinates']['coordinates'])
        if (counter % 20 == 0):
            print (dateutil.parser.parse(item['created_at']))

        counter += 1
        AppendTwitte(item)


if __name__ == '__main__':
    sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='backslashreplace')
    argvs = sys.argv
    argc = len(argvs)
    sys.exit(main(argvs, argc))
