#!/usr/bin/python
import cgi
import cgitb; cgitb.enable()
import regenerate
import os

form = cgi.FieldStorage()
surTitle = form.getvalue("survey_name")
userID = form.getvalue("newID")

f = open("survey.ssv", "r")
new = open("survey_new.ssv", "w")

line = f.readline()
while(line.rstrip() != userID):
	new.write(line)
	line = f.readline()
	if line == "":
		break
	
if line != "":
	while(line.rstrip() != "***END***"):
		
		line = f.readline()
	line = f.readline()
	while line != "":
		new.write(line)
		line = f.readline()
	new.write(userID+"\n")
	new.write(surTitle+"\n")
else:
	new.write(userID+"\n")
	new.write(surTitle+"\n")
new.close()
f.close()
os.remove("survey.ssv")
os.rename("survey_new.ssv", "survey.ssv")


regenerate.regenerate(userID,surTitle,"newSur")
