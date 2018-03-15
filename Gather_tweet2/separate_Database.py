# -*- coding: utf-8 -*-
import sys
import codecs
from twitter_db import *
reload(sys)
sys.setdefaultencoding('utf-8')
from collections import defaultdict
from datetime import datetime as dt
import json

def main(argvs, argc):

    start_date = "2016/11/09 03:01:00"
    end_date = "2016/11/09 03:54:00"
    interval = 60

    tweets = GetTwittes(start_date, end_date)
    #print(tweets)
    #print dir(tweets)

    #f = open('contents.txt', 'w') #ファイルが無ければ作る、の'a'を指定します

    hrmi_pre = '03:01'
    counter = 0
    ite = 0
    dict = {}
    tmpstr = ''

    for tw in tweets:
        #print tw.id
        ite = ite + 1
        try:
            text = tw.contents.decode('cp932')
        except:
            x = 1
            #print('error' + str(ite))
        else:
    	    new_time = tw.createAt.encode('utf-8')
    	    hrmi = new_time[11:16]

    	    if (hrmi != hrmi_pre):
        		hrmi_pre = hrmi
        		dict[counter] = tmpstr
        		counter = counter + 1
        		tmpstr = ''

        		#print hrmi
        		print counter

    	    else:
        		tmpstr = tmpstr + text

    print len(dict)
    f = open("output_later.json", "w")
    json.dump(dict, f)
    f.close()

if __name__ == '__main__':
    #sys.stdout = codecs.getwriter(sys.stdout.encoding)(sys.stdout, errors='backslashreplace')
    argvs = sys.argv
    argc = len(argvs)
    sys.exit(main(argvs, argc))
