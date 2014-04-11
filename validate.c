#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define EXTRA 8
#define MAXLENGTH_ID 20
#define MAXLENGTH_PWD 20


int validate(char *id, char *pwd)
{
	char buffer[200];
	char *acc, *pass;

	FILE *in = fopen("members.ssv", "r");
	fgets(buffer, sizeof(buffer), in);

	while(!feof(in))
	{
		acc=strtok(buffer," ");
		pass=strtok(NULL, " ");
		
		if (strncmp(id, acc, strlen(id))==0 && strncmp(pwd, pass, strlen(pwd)) == 0)
			return 1;
		fgets(buffer, sizeof(buffer), in);
	}
	fclose(in);
	return 0;
}

int unencode(char *src, char *last, char *loginid, char *loginpwd)
{
	
	char *id=loginid;
	char *pwd=loginpwd;

	for(; src != last; src++, id++){
		if(*src == '+') //input contains a space - not allowed
			return 0;
		else if(*src == '%') 
			return 1; //ID contains a special character (other than -, _, and .) - not allowed
		else if (*src == '&')
		{
			src++;
			break;
		}
		else
		{
			*id = *src;
		}
	}

	src+=9;

	for (; src != last; src++, pwd++)
	{
		if(*src== '+')
			return 0;
		else 
		{
			*pwd = *src;
		}
	}

	
	*id = '\0';
	
	*pwd = '\0';

	return 2;
}

int main(void){
	char *lenstr;
	char raw_input[200];
	char *id;
	char *pwd;
	long len;
	int unencoded, value;

	id = malloc(MAXLENGTH_ID+1);
	pwd = malloc(MAXLENGTH_PWD+1);

	lenstr = getenv("CONTENT_LENGTH");
	

	printf("%s%c%c\n", "Content-Type:text/html;charset=iso-8879-1", 13, 10);
	printf("<title>Pollymorph</title>\n");
	printf("<head><link rel=\"stylesheet\" href=\"http://cs.mcgill.ca/~cliu65/Pollymorph/style.css\" type=\"text/css\"></link>\n");
	printf("<link rel=\"stylesheet\" href=\"style_login.css\" type=\"text/css\"></link>\n");
	printf("<link href='http://fonts.googleapis.com/css?family=Alegreya+Sans:400,500,700,800,900,400italic,500italic,700italic,800italic,900italic' rel='stylesheet' type='text/css'></head>\n");
	printf("<body><div id=\"topHalf\" class=\"wrap\">\n");


	if (lenstr==NULL || sscanf(lenstr,"%ld", &len)!=1 ||  len>66)
	{

		printf("		<div id=\"loginbuttons\" >\n");
		printf("			<a href=#>\n");
		printf("			<div class=\"smallbutton2\" >\n");
		printf("				<b>fill out a survey</b></div></a></div>\n");
		printf("		<a href=\"http://www.cs.mcgill.ca/~cliu65/Pollymorph/survey.py\">\n");
		printf("			<div id=\"header\" >\n");
		printf("			<img id=\"logo\" src=\"logo.png\"></div></a></div>\n");
		printf("	<div id=\"content\" class=\"wrap\"><br><br>\n");
		printf("<h3>Wrong form error: please log in from the log in page.</h3>");
		printf("			<br><br><a href=\"http://www.cs.mcgill.ca/~syou3/Pollymorph/login.html\">\n");
		printf("			<div class=\"bigbox\" id=\"leftbb\">\n");
		printf("				<h1>login</h1>\n");
		printf("			</div></a><br><br>\n");		

	}
	else
	{
	
		fgets(raw_input, len+1, stdin); //""
		
		unencoded = unencode(raw_input+EXTRA, raw_input+len, id, pwd);
		
		//in case of incorrect format, create a warning page with a "back" button
		if (validate(id, pwd))
			{
				printf("		<div id=\"loginbuttons\" >\n");
				printf("			<a href=\"http://www.cs.mcgill.ca/~cliu65/Pollymorph/welcome.html\">\n");
				printf("			<div class=\"smallbutton2\" >\n");
				printf("				<b>log out</b></div></a></div>\n");
				printf("		<a href=\"http://www.cs.mcgill.ca/~cliu65/Pollymorph/welcome.html\">\n");
				printf("			<div id=\"header\" >\n");
				printf("			<img id=\"logo\" src=\"logo.png\"></div></a></div>\n");
				printf("	<div id=\"content\" class=\"wrap\"><br><br>\n");
			
				printf("		You have been successfully logged in as <strong>%s.<br><br>\n", id);
				printf("		<form name=\"toCreateSurvey\" action=\"http://cs.mcgill.ca/~schen89/createSurvey.py\"  method=\"post\">\n"); //UPDATE ACTION ROUTE
				printf("			<input type=\"hidden\" name=\"userID\" value=\"%s\">\n\n", id);
				printf("		</form>\n");
				printf("		<form name=\"toSurvey\" action=\"http://cs.mcgill.ca/~cliu65/Pollymorph/survey.py\"  method=\"post\">\n");
				printf("			<input type=\"hidden\" name=\"userID\" value=\"%s\">\n", id);
				printf("		</form>\n");
			}
		else
		{
			printf("		<div id=\"loginbuttons\" >\n");
			printf("			<a href=#>\n");
			printf("			<div class=\"smallbutton2\" >\n");
			printf("				<b>fill out a survey</b></div></a></div>\n");
			printf("		<a href=\"http://www.cs.mcgill.ca/~cliu65/Pollymorph/survey.py\">\n");
			printf("			<div id=\"header\" >\n");
			printf("			<img id=\"logo\" src=\"logo.png\"></div></a></div>\n");
			printf("	<div id=\"content\" class=\"wrap\"><br><br>\n");

			if (!strcmp(raw_input, "loginID=&loginpwd=")) //empty input
				printf("		Please make sure your ID and password are at least 8 characters long each.");
			else if (unencoded==0)
				printf("		Please do not use any spaces.\n");
			else if (unencoded==1)
				printf("		Please only use the alphabet, numbers, ., -, and/or _ in your ID.\n");
			else
				printf("		Your ID and password do not match.");

			printf("			<br><br><a href=\"http://www.cs.mcgill.ca/~syou3/Pollymorph/login.html\">\n");
			printf("			<div class=\"bigbox\" id=\"leftbb\">\n");
			printf("				<h1>go back</h1>\n");
			printf("			</div></a><br><br>\n");

		}

	}
	
	printf("<a href=#><div class=\"bigbox\" onClick=\"document.forms['toCreateSurvey'].submit();\" id=\"leftbb\">\n");
	printf("<h1>Create Survey</h1>\n");
	printf("</div></a>\n\n");
	
	printf("<a href=#><div class=\"bigbox\" onClick=\"document.forms['toSurvey'].submit();\" id=\"rightbb\">\n");
	printf("<h1>Fill out a Survey</h1>\n");
	printf("</div></a><br>\n");


	printf("<a href=\"http://cs.mcgill.ca/~cliu65/Pollymorph/welcome.html\">\n");
	printf("<div class=\"bigbox\" id=\"leftbb\"><h1>Return Home</h1></div></a>\n\n");





	printf("</div></body>\n");


	return 0;}