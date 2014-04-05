#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import regenerate
    

form = cgi.FieldStorage()
surveyTitle = form.getvalue("survey_name")

f = open("survey.ssv", "w")
f.write(surveyTitle)
f.write("\n")
f.close()




regenerate.regenerate(surveyTitle,"newSur")
