#!/usr/bin/python

import cgi
import urllib
import os


def saveResults(form, userid):
	#open old file for reading
	old = open("results.ssv", "r")
	#open new file for writing
	new = open("results_new.ssv", "w")
	#copy all lines except the survey we're saving from, save it to the end
	copyResults = []
	line = old.readline()
	# copy entries before survey
	while line.rstrip() != userid:
		new.write(line)
		line = old.readline()
		if line == "":
			break
	
	if line != "":
		#save survey entries to list
		while line.rstrip() != "***END***":
			copyResults.append(line)
			line = old.readline()
		
		# copy entries after survey
		line = old.readline()   #offset one after 
		while line != "":
			new.write(line)
			line = old.readline()
		# appen survey to the end
		for restore in copyResults:
			new.write(restore)
		# add this submit and close
	else:
		new.write(userid+"\n")
	for key in form.keys():
		if key != 'userID':
			new.write(form[key].value+" ")
	new.write("\n***END***\n")
	new.close()	
	old.close()
	os.remove("results.ssv")
	os.rename("results_new.ssv", "results.ssv")

def getQuestion(n, userid):
	urllib.urlcleanup()
	#result = urllib.urlopen('http://cs.mcgill.ca/~cliu65/Pollymorph/results.ssv')
	result = open("results.ssv", "r")
	count = [0,0,0,0]
	line = result.readline()
	# move cursor to this user
	while line.rstrip() != userid:
		line = result.readline()
	line = result.readline() # offset after 1
	while line.rstrip() != "***END***":
		user = line.split(" ")
		count[int(user[n-1])-1] += 1	
		line = result.readline()
	result.close()
	return count
		

def displayResults(form, userid):
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
	
	#survey  = urllib.urlopen('http://cs.mcgill.ca/~cliu65/Pollymorph/survey.ssv')
	survey = urllib.urlopen('http://cs.mcgill.ca/~schen89/survey.ssv')
	questions = survey.readline()
	# move cursor to userid
	while questions.rstrip() != userid:
		questions=survey.readline()
		if questions == "":
			return
	id = questions.rstrip()
	title = survey.readline()
	i = 1
	questions=survey.readline()
	while questions.rstrip() != "***END***":
		count = getQuestion(i, userid)
		print "<tr>\n"
		print "<td>"+str(i)+".</td>\n"
		print "<td class=\"nocenter\">"+questions.rstrip()+"</td>\n"	
		print "<td>"+str(count[3])+"</td>\n"
		print "<td>"+str(count[2])+"</td>\n"
		print "<td>"+str(count[1])+"</td>\n"
		print "<td>"+str(count[0])+"</td>\n"
		print "</tr>\n"
		questions = survey.readline()
		i = i+1
	print "</table>\n"
	print "</div><br><br><br>"
	print '<a href="http://cs.mcgill.ca/~cliu65/Pollymorph/welcome.html">'
	print '<div class="bigbox4" id="home">'
	print '<h2>Return Home</h2>'
	print '</div>'
	print '</a>'
	print '</div>'
	print '</body></html>'
	survey.close()

def main():
	print "Content-Type: text/html\n\n"
	userid="guest"
	form = cgi.FieldStorage()
	if form.has_key('userID'):
		userid = form['userID'].value
	if form.has_key('opinion1'):
		saveResults(form, userid)
	displayResults(form, userid)

main()
