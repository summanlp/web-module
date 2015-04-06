#! /usr/bin/env python

import web
import json

# Imports files from a parent directory.
from summa.summarizer import summarize
from summa.keywords import keywords

render = web.template.render('templates/', base='layout')
urls = (
    '/', 'autosummarize',
    '/foo','foo',
    '/gexf','gexf'
)
LANGUAGES = {
    'danish': 'Danish',
    'dutch': 'Dutch',
    'english': 'English',
    'finnish': 'Finnish',
    'french': 'French',
    'german': 'German',
    'hungarian': 'Hungarian',
    'italian': 'Italian',
    'norwegian': 'Norwegian',
    'porter': 'Porter',
    'portuguese': 'Portuguese',
    'romanian': 'Romanian',
    'russian': 'Russian',
    'spanish': 'Spanish',
    'swedish': 'Swedish'
}

class foo:
	def GET(self):
		lista = [1,3,5,7]
		web.header('Content-Type', 'application/json')
		return json.dumps({"data":lista})
        
       
class autosummarize:
    def GET(self):
        return render.autosummarize(languages=LANGUAGES) 
        
    def POST(self):
        args = web.input()
        show_scores = "scores" in args
        length = int(args.length) / 100.0
        language = args.language
        text = args.text
        method = summarize if args.type == "summarize" else keywords

        result = method(text=text, ratio=length, language=language, scores=show_scores)
        return render.autosummarize(summary=result)


class gexf:
    def GET(self):
    	return render.gexf()


app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

wsgiapp = app.wsgifunc()
