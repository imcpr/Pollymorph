#!/usr/bin/python

import regenerate
import cgitb; cgitb.enable()
import cgi
form = cgi.FieldStorage()

surveyTitle = form.getvalue("surveyTitle")
userID = form.getvalue("addID")
f = open("survey.ssv", "a")
f.write(form.getvalue("question_name"))
f.write("\n")
f.close()




regenerate.regenerate(userID,surveyTitle,"addQ")
