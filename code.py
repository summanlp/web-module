#! /usr/bin/env python

import web
import json
from textrank import textrank

PATH_DEFAULT_TEXT = "textrank/test_data/textrank_example.txt"

render = web.template.render('templates/', base='layout')
urls = (
  '/', 'index',
  '/foo','foo',
  '/autosummarize', 'autosummarize'
)

class index:
    def GET(self):
    	print "holamundo" 
    	return render.index()
		

class foo:
	def GET(self):
		lista = [1,3,5,7]
		web.header('Content-Type', 'application/json')
		return json.dumps({"data":lista})
        
       
class autosummarize:
    def GET(self):
        with open(PATH_DEFAULT_TEXT) as fp:
            text = fp.read()
        return render.autosummarize(default_text=text) 
        
    def POST(self):
        textarea = web.input(id="text")
        summary = textrank.textrank(text=textarea.text)
        return render.autosummarize(summary=summary) 


	def POST(self):
		req = web.input()
		print req
		res = {"nombre": req.name}
		web.header('Content-Type', 'application/json')
		return json.dumps(res)



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
