# -*- coding: utf-8 -*-
import nltk
import json

#raw = open('contents.txt').read()
f = open("output.json")
data = json.load(f)
#print data.keys()
dict = {}
print(len(data))

for i in range(0,len(data)):
	print i
	st = str(i)
	#print type(data[st])
	#new = unicode(data[st], 'utf_8')
	new = data[st]

	tokens = nltk.word_tokenize(new)
	#print type(tokens)
	#print tokens
	#print len(tokens)

	text = nltk.Text(tokens)
	#print text.concordance('Florida', lines=10)

	#stopwords = nltk.corpus.stopwords.words('english')
	#symbols = ["'", '"', '`', '.', ',', '-', '!', '?', ':', ';', '(', ')','#','@','%','https','rt','ap','...','\'s']
	states = ['alabama','alaska','arizona','arkansas','california','colorado','connecticut','delaware','florida','georgia','hawaii','idaho','illinois','indiana','iowa','kansan','kentucky','lousiana','maine','maryland','massachusetts','michigan','minnesota','mississippi','missouri','montana','nebraska','nevada','hampshire','jersey','mexico','york','carolina','dakota','ohio','oklahoma','oregon','pennsylvania','rhode','tennessee','texas','utah','vermont','virginia','washington','wisconsin','wyoming']
	important = ['trump','clinton','grate','donald','hillary','democrat','republican']
	fdist = nltk.FreqDist(w.lower() for w in text if w.lower() in states + important)

	dict[st] = fdist.items()

	#print fdist.items()[:50]
	#fdist.plot(cumulative=False)

#print len(dict)
f = open("hist_per_minute.json", "w")
json.dump(dict, f)
f.close()
