#! /usr/bin/env python

import web

import json

render = web.template.render('templates/', base='layout')
urls = (
  '/', 'index',
  '/foo','foo'
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


	def POST(self):
		req = web.input()
		print req
		res = {"nombre": req.name}
		web.header('Content-Type', 'application/json')
		return json.dumps(res)



if __name__ == "__main__":
    app = web.application(urls, globals())
    app.run()
