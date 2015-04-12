#! /usr/bin/env python

import web
import json
import time
from os import system
from summa.summarizer import summarize
from summa.keywords import keywords
from summa.export import gexf_export

render = web.template.render('templates/', base='layout')
urls = (
    '/', 'autosummarize',
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

def format_results(result, show_scores, method):
    separator = "<br>" if method == "summarize" else "<br> - "
    result = ["{:.3f}".format(score) + " - " + phrase for phrase, score in result ]if show_scores else result
    return separator[4:] + separator.join(result)



class autosummarize:
    def GET(self):
        return render.autosummarize(languages=LANGUAGES) 
        
    def POST(self):
        args = web.input()
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

    def POST(self):
        args = web.input()
        language = args.language
        text = args.text
        by_sentence, by_word = (True, False) if args.method == "summarize" else (False, True)
        path = "export-" + str(time.time()) + ".gexf"
        gexf_export(text=text, path=path, language=language, by_sentence=by_sentence, by_word=by_word)
        system("mv {0} static/{0}".format(path))
        return render.gexf(path="./static/" + path)


app = web.application(urls, globals())

if __name__ == "__main__":
    app.run()

wsgiapp = app.wsgifunc()
