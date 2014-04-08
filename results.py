#!/usr/bin/python

import cgi
import urllib


def saveResults(form):
	file = open("results.ssv", "a")
	for key in form.keys():
		file.write(form[key].value+" ")
	file.write("\n")
	file.close()	

def getQuestion(n):
	result = urllib.urlopen('results.ssv')
	count = [0,0,0,0]
	line = result.readline()
	while line != "":
		user = line.split(" ")
		count[int(user[n-1])-1] += 1	
		line = result.readline()
	result.close()
	return count
		

def displayResults(form):
	#grab header+half the table from template page
	resultsPage = urllib.urlopen('http://cs.mcgill.ca/~syou3/Pollymorph/results.html')
	line = resultsPage.readline()
	while '</tr>' not in line:
		if '<h1>Is COMP' not in line:
			print line
		line = resultsPage.readline()
	print '</tr>'
	resultsPage.close()
	# done with table, dynamic content here
	
	survey  = urllib.urlopen('http://cs.mcgill.ca/~schen89/survey.ssv')
	questions = survey.readlines()
	for i in range (1, len(questions)):
		count = getQuestion(i)
		print "<tr>\n"
		print "<td>"+str(i)+".</td>\n"
		print "<td class=\"nocenter\">"+questions[i]+"</td>\n"	
		print "<td>"+str(count[3])+"</td>\n"
		print "<td>"+str(count[2])+"</td>\n"
		print "<td>"+str(count[1])+"</td>\n"
		print "<td>"+str(count[0])+"</td>\n"
		print "</tr>\n"
	print "</table>\n"
	print "</div><br><br><br>"
	print '<a href="http://cs.mcgill.ca/~cliu65/Pollymorph/welcome.html">'
	print '<div class="bigbox4" id="home">'
	print '<h2>Return Home</h2>'
	print '</div>'
	print '</a>'
	print '</div>'
	print '</body></html>'

def main():
	print "Content-Type: text/html\n\n"
	form = cgi.FieldStorage()
	if form:
		saveResults(form)
	displayResults(form)

main()
