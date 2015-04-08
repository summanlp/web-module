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

    def POST(self):
        input = web.input()
        print input
        return "the whole summary goes here"


def format_results(result, show_scores, method):
    separator = "<br>" if method == "summarize" else "<br> - "
    result = ["{:.3f}".format(score) + " - " + phrase for phrase, score in result ]if show_scores else result
    return separator[4:] + separator.join(result)



class autosummarize:
    def GET(self):
        return render.autosummarize(languages=LANGUAGES) 
        
    def POST(self):
        args = web.input()
        print args
        show_scores = args.scores == "true"
        length = int(args.length) / 100.0
        language = args.language
        text = args.text
        method = summarize if args.method == "summarize" else keywords

        try:
            result = method(text=text, ratio=length, language=language, split=True, scores=show_scores)
            return format_results(result, show_scores, args.method)
        except:
            return ""




class gexf:
    def GET(self):
        return render.gexf()


app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

wsgiapp = app.wsgifunc()
