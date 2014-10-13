#! /usr/bin/env python

import web

import json

render = web.template.render('templates/')
urls = (
  '/', 'index',
  '/foo','foo',
  '/autosummarize', 'autosummarize'
)

class index:
    def GET(self):
    	return render.index()
		

class foo:
	def GET(self):
		lista = [1,3,5,7]
		web.header('Content-Type', 'application/json')
		return json.dumps({"data":lista})
        
        
class autosummarize:
    def GET(self):
        return render.autosummarize()       
        
    def POST(self):
        return web.data()


if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
