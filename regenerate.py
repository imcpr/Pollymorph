#!/usr/bin/python

def regenerate(title,function):
        create = open("createSurvey.html","r")
        lines = create.readlines()
        print "Content-type:text/html\r\n\r\n"
        if(function == "newSur"):
            for line in lines:
                if(line == '<b>Create a New Survey</b>\n'):
                        print '<b>Survey Title: &nbsp &nbsp %s</b>\n' %title
                elif(line == '<input type="hidden" name="surveyTitle" value="survey_name">\n'):
                        print '<input type="hidden" name="surveyTitle" value="%s">\n' %title
        
                elif(line == '<p><form class="this" action="newSurvey.py" method="post" margin="0px">\n'):
                        print "\n"
                elif(line == '<input type="text" name="survey_name" style="color:#888; width:270px; position:relative;"value="Enter the title of the survey" onfocus="inputFocus(this)" onblur="inputBlur(this)" />\n'):
                        print "\n"
                elif(line == '<input type="submit" value="NEW"></form></p>\n'):
                        print "\n"
                elif(line == '<p><form action="endSurvey.py" method="post"><input type="submit" value="DONE"><input type="hidden" name="surveyName" value="survey_name"></form></p>\n'):
                        print '<p><form action="endSurvey.py" method="post"><input type="submit" value="DONE"><input type="hidden" name="surveyName" value="%s"></form></p>\n' %title
                else:
                    print '%s' %line
            
            
        if(function == "addQ"):
                g = open("survey.ssv", "r")
                g.readline()
                i=1
                for line in lines:
                        if(line == '<b>Create a New Survey</b>\n'):
                                print '<b> Survey Title: &nbsp &nbsp %s</b>\n' %title
                                print '<small>'
                                print '<ul>'
                                for question in g:
                                        print '<li>Question &nbsp %d: %s </br></li>\n' %(i,question)
                                        i=i+1
                                print '</ul>'
                                print '</small>\n'
                                
                        elif(line == '<input type="hidden" name="surveyTitle" value="survey_name">\n'):
                                print '<input type="hidden" name="surveyTitle" value="%s">\n' %title
                        elif(line == '<p><form class="this" action="newSurvey.py" method="post" margin="0px">\n'):
                                print "\n"
                        elif(line == '<input type="text" name="survey_name" style="color:#888; width:270px; position:relative;"value="Enter the title of the survey" onfocus="inputFocus(this)" onblur="inputBlur(this)" />\n'):
                                print "\n"
                        elif(line == '<input type="submit" value="NEW"></form></p>\n'):
                                print "\n"
                        elif(line == '<p><form action="endSurvey.py" method="post"><input type="submit" value="DONE"><input type="hidden" name="surveyName" value="survey_name"></form></p>\n'):
                                print '<p><form action="endSurvey.py" method="post"><input type="submit" value="DONE"><input type="hidden" name="surveyName" value="%s"></form></p>\n' %title
                        else:
                            print '%s' %line

                g.close()

        if(function == "endSur"):
                g = open("survey.ssv", "r")
                g.readline()
                i=1
                for line in lines:
                        if(line == '<b>Create a New Survey</b>\n'):
                                print '<b> Survey Title: &nbsp &nbsp %s</b>\n' %title
                                print '<small>'
                                print '<ul>'
                                for question in g:
                                        print '<li>Question &nbsp %d: %s </br></li>\n' %(i,question)
                                        i=i+1
                                print '</ul>'
                                print '</small>\n'
                                print '<center><a href="http://cs.mcgill.ca/~cliu65/Pollymorph/welcome.html"><button>HOME PAGE</button></a> &nbsp&nbsp&nbsp&nbsp\n'
                                print '<a href="http://cs.mcgill.ca/~cliu65/Pollymorph/takeSurvey.html"><button>TAKE SURVEY</button></a>&nbsp&nbsp&nbsp&nbsp\n'
                                print '<a href="http://www.cs.mcgill.ca/~schen89/createSurvey.html"><button>CREATE SURVEY</button></a></center>&nbsp&nbsp&nbsp&nbsp\n'
                                
                        elif(line == '<input type="hidden" name="surveyTitle" value="survey_name">\n'):
                                print '<input type="hidden" name="surveyTitle" value="%s">\n' %title
                        elif(line == '<p><form class="this" action="newSurvey.py" method="post" margin="0px">\n'):
                                print "\n"
                        elif(line == '<input type="text" name="survey_name" style="color:#888; width:270px; position:relative;"value="Enter the title of the survey" onfocus="inputFocus(this)" onblur="inputBlur(this)" />\n'):
                                print "\n"
                        elif(line == '<input type="submit" value="NEW"></form></p>\n'):
                                print "\n"
                        elif(line == '<p><form class="this" action="addQuestion.py" method="post" margin="0px">\n'):
                                print "\n"
                        elif(line == '<input type="text" name="question_name" style="color:#888; width:270px; position:relative;"value="Enter a new survey question" onfocus="inputFocus(this)" onblur="inputBlur(this)" />\n'):
                                print "\n"
                        elif(line == '<input type="submit" value="ADD">\n'):
                                print "\n"
                        elif(line == '<input type="hidden" name="surveyTitle" value="survey_name"></form></p>\n'):
                                print "\n"
                        elif(line == '<p><form action="endSurvey.py" method="post"><input type="submit" value="DONE"><input type="hidden" name="surveyName" value="survey_name"></form></p>\n'):
                                print "\n"
                        else:
                                print '%s' %line

                g.close()
                
        create.close()
        
if __name__ == "__main__":
       regenerate(title,function)
