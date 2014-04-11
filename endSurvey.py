#!/usr/bin/python
import regenerate
import cgi
import cgitb; cgitb.enable()


form = cgi.FieldStorage()
surveyTitle = form.getvalue("surveyName")
userID = form.getvalue("endID")
f = open("survey.ssv","a")
f.write("***END***\n")

regenerate.regenerate(userID,surveyTitle,"endSur")
