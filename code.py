#! /usr/bin/env python

import web
import json
import sys, os

# Imports files from a parent directory.
sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), os.pardir, 'textrank'))
from summa.summarizer import summarize as textrank
from summa import summarizer, keywords

render = web.template.render('templates/', base='layout')
urls = (
    '/', 'autosummarize',
    '/foo','foo',
    '/gexf','gexf'
)		

class foo:
	def GET(self):
		lista = [1,3,5,7]
		web.header('Content-Type', 'application/json')
		return json.dumps({"data":lista})
        
       
class autosummarize:
    def GET(self):
        return render.autosummarize() 
        
    def POST(self):
        textarea = web.input()
        print textarea
        summary = summarizer.summarize(text=textarea.text)
        return render.autosummarize(summary=summary)


class gexf:
    def GET(self):
    	return render.gexf()


app = web.application(urls, globals())
wsgiapp = app.wsgifunc()
