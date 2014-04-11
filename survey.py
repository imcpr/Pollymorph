#!/usr/bin/python

import cgi
import urllib

def getHeader():
	headerPage = urllib.urlopen('http://cs.mcgill.ca/~cliu65/Pollymorph/takeSurvey.html')
	line = headerPage.readline()
	while '<h1>' not in line:
		print line
		line = headerPage.readline()
	headerPage.close()

def getSurvey(userid):
	#surveyPage = urllib.urlopen('http://cs.mcgill.ca/~cliu65/Pollymorph/survey.ssv')
	surveyPage = urllib.urlopen('http://cs.mcgill.ca/~schen89/survey.ssv')
	id = surveyPage.readline().rstrip()
	while id != userid:
		if id == "":
			break
		id = surveyPage.readline().rstrip()
	
	if id=="":
		print '<div style="cursor:pointer" onclick="document.forms[\'myform\'].submit();" ><h1>'+userid+', you have no survey record, please click HERE to create one first</h1></div>'
		print '<form name="myform" method="post" action="http://cs.mcgill.ca/~schen89/createSurvey.py"><input type="hidden" name="userID" value="'+userid+'"></form>'
		surveyPage.close()
		return
	#raw_input()
	title = surveyPage.readline()
	print "<h1>"+title+"</h1>\n"
	print '<form action="results.py" method="post">'
	question = surveyPage.readline().rstrip()
	d = 1
	while question != "***END***":
		print "<b>"+question.rstrip()+"</b><br>\n"
		n = str(d)
		print "<input type=\"radio\" name=\"opinion"+n+"\" value=\"4\">Disagree Strongly<input type=\"radio\" name=\"opinion"+n+"\" value=\"3\">Disagree<input type=\"radio\" name=\"opinion"+n+"\" value=\"2\">Agree<input type=\"radio\" name=\"opinion"+n+"\" value=\"1\">Agree Strongly<br><br>"
		d = d+1
		question = surveyPage.readline().rstrip()
		#raw_input()
	print '<input type="hidden" name="userID" value="' + userid + '">'
	print '<br><br><input type="submit">'
	print '</form>'
	surveyPage.close()
	#missing view result
	print '<div style="cursor:pointer" onclick="document.forms[\'myform2\'].submit();" id="resultbutton"><p>View results</p></div>'
	print '<form name="myform2" method="post" action="results.py"><input type="hidden" name="userID" value="'+userid+'"></form>'
def getFooter():
	print "</div>\n"	
	print '<div id="footer" class="wrap"><p>Brought to you by team CASper - Casper, Allen and Suzin</p></div>'
	print '</body>'
	print '</html>'



def main():
	userid="guest"
	print "Content-Type: text/html\n\n"
	form = cgi.FieldStorage()
	if form:
		userid = form['userID'].value
	getHeader()
	getSurvey(userid)
	getFooter()

main()



