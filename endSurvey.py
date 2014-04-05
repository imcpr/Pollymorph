#!/usr/bin/python
import regenerate
import cgi
import cgitb; cgitb.enable()


form = cgi.FieldStorage()
surveyTitle = form.getvalue("surveyName")

regenerate.regenerate(surveyTitle,"endSur")
