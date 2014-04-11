#!/usr/bin/python

import cgitb; cgitb.enable()
import cgi

form = cgi.FieldStorage()

ID = form.getvalue("userID")

def generate(ID):
    page = open("createSurvey.html","r")
    print "Content-type:text/html\r\n\r\n"
    lines = page.readlines()
    for line in lines:
        
        if(line == '<input type="hidden" name="addID" value="ID">\n'):
            print '<input type="hidden" name="addID" value="%s">\n' %ID
        elif(line == '<input type="hidden" name="surveyTitle" value="survey_name"><input type="submit" value="ADD"></form></p>\n'):
            print "\n"
        elif(line == '<p><form action="endSurvey.py" method="post"><input type="hidden" name="endID" value="user_ID"><input type="submit" value="DONE"><input type="hidden" name="surveyName" value="survey_name"></form></p>\n'):
            print "\n"
        elif(line == '<input type="hidden" name="newID" value="ID">\n'):
            print '<input type="hidden" name="newID" value="%s">\n' %ID
        elif(line == '<p><form class="this" action="addQuestion.py" method="post" margin="0px">\n'):
            print "\n"
        elif(line == '<input type="text" name="question_name" style="color:#888; width:270px; position:relative;"value="Enter a new survey question" onfocus="inputFocus(this)" onblur="inputBlur(this)" />\n'):
            print "\n"
        elif(line == '<p><form action="endSurvey.py" method="post"><input type="hidden" name="endID" value="user_ID"><input type="submit" value="DONE"><input type="hidden" name="surveyName" value="survey_name"></form></p>\n'):
            print "\n"
        else:
            print '%s' %line
    page.close()

if __name__ == "__main__":
    generate(ID)
