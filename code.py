#! /usr/bin/env python

import web
import json

PATH_DEFAULT_TEXT = "textrank/test_data/textrank_example.txt"

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
        
    # def POST(self):
    #     textarea = web.input(id="text")
    #     summary = textrank.textrank(text=textarea.text)
    #     return render.autosummarize(summary=summary) 

    def POST(self):
        req = web.input()
        print req
        web.header('Content-Type', 'application/json')
        return json.dumps(res)

class gexf:
    def GET(self):
    	return render.gexf()



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
