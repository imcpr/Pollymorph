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

def getSurvey():
	surveyPage = urllib.urlopen('http://cs.mcgill.ca/~schen89/survey.ssv')
	title = surveyPage.readline()
	print "<h1>"+title+"</h1>\n"
	print '<form action="results.py" method="post">'
	question = surveyPage.readline()
	d = 1
	while question != "":
		print "<b>"+question.rstrip()+"</b><br>\n"
		n = str(d)
		print "<input type=\"radio\" name=\"opinion"+n+"\" value=\"4\">Disagree Strongly<input type=\"radio\" name=\"opinion"+n+"\" value=\"3\">Disagree<input type=\"radio\" name=\"opinion"+n+"\" value=\"2\">Agree<input type=\"radio\" name=\"opinion"+n+"\" value=\"1\">Agree Strongly<br><br>"
		d = d+1
		question = surveyPage.readline()
		
	print '<br><br><input type="submit">'
	print '</form>'
	surveyPage.close()
	#missing view result
	print '<a href="results.py"><div id="resultbutton"><p>View results</p></div></a>'
def getFooter():
	print "</div>\n"	
	print '<div id="footer" class="wrap"><p>Brought to you by team CASper - Casper, Allen and Suzin</p></div>'
	print '</body>'
	print '</html>'



def main():
	print "Content-Type: text/html\n\n"
	getHeader()
	getSurvey()
	getFooter()

main()



