#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#define EXTRA 3
#define MAXLENGTH_ID 20
#define MAXLENGTH_PWD 20

int unencode(char *src, char *last, char *newid, char *newpwd, char *renewpwd, char *newemail)
{
	char *id=newid;
	char *pwd=newpwd;
	char *rpwd=renewpwd;
	char *email=newemail;
	
	int i=0;
	int j=0;
	int k=0;

	for(; src != last; src++, id++){
		if(*src == '+') //input contains a space - not allowed
			return 0;
		else if(*src == '%') 
			return 1; //ID contains a special character (other than -, _, and .) - not allowed
		else if (*src == '&'){
			src++;
			break;
		}
		else{
			*id = *src;
			i++;
		}
	}
	//printf("\nid:  i=%d and then increment<br><br>\n\n",i);
	src+=4; //skip "pwd="
	
	for (; src != last; src++, pwd++){
		if(*src== '+')
			return 0;
		else if (*src == '&'){
			src++;
			break;
		}
		else {
			*pwd = *src;
			j++;
		}
	}
	//printf("\npwd: count j=%d and then increment<br><br>\n\n",j);
	src+=5; //skip "rpwd="

	for(; src != last; src++, rpwd++){
		if(*src== '+')
			return 0;
		else if (*src == '&'){
			src++;
			break;
		}
		else {
			*rpwd = *src;
			k++;
			//printf("rpwd count %d<br>",k);
		}		
	}
	//printf("\nrpwd:count k=%d and then increment<br><br>\n\n",k);
	src+=6;//skip "email="

	for (; src != last; src++, email++)
	{
		if(*src== '+')
			return 0;
		else {
			*email = *src;
		}
	}
	//printf("\nemail: count = and then increment<br><br>\n\n");
	*id = '\0';
	
	*pwd = '\0';
	
	*rpwd = '\0';
	
	*email = '\0';

	return 2;
}


int main(void)
{
	char *lenstr;
	char raw_input[200];
	char *id;
	char *pwd;
	char *rpwd;
	char *email;
	long len;

	FILE *in = fopen("members.ssv", "a");
	
	id = malloc(MAXLENGTH_ID+1);
	pwd = malloc(MAXLENGTH_PWD+1);
	rpwd = malloc(MAXLENGTH_PWD+1);
	email = malloc(100);

	lenstr = getenv("CONTENT_LENGTH");
	

	printf("%s%c%c\n", "Content-Type:text/html;charset=iso-8879-1", 13, 10);
	printf("<title>Pollymorph</title>\n");
	printf("<head><link rel=\"stylesheet\" href=\"http://cs.mcgill.ca/~cliu65/Pollymorph/style.css\" type=\"text/css\"></link>\n");
	printf("<link rel=\"stylesheet\" href=\"style_login.css\" type=\"text/css\"></link>\n");
	printf("<link href='http://fonts.googleapis.com/css?family=Alegreya+Sans:400,500,700,800,900,400italic,500italic,700italic,800italic,900italic' rel='stylesheet' type='text/css'></head>\n");
	printf("<body><div id=\"topHalf\" class=\"wrap\">\n");
	printf("		<div id=\"loginbuttons\" >\n");
	printf("			<a href=#>\n");
	printf("			<div class=\"smallbutton2\" >\n");
	printf("				<b>create new survey</b></div></a></div>\n");
	printf("		<a href=\"http://www.cs.mcgill.ca/~schen89/createSurvey.html\">\n");
	printf("			<div id=\"header\" >\n");
	printf("			<img id=\"logo\" src=\"logo.png\"></div></a></div>\n");
	printf("	<div id=\"content\" class=\"wrap\"><br><br>\n");







	if (lenstr==NULL || sscanf(lenstr,"%ld", &len)!=1 ||  len>MAXLENGTH_ID+2*MAXLENGTH_PWD+100)
	{
		printf("<h3>Please make sure your ID and password are no more than 20 characters long.</h3>");
		printf("			<br><br><a href=\"http://www.cs.mcgill.ca/~syou3/Pollymorph/login.html\">\n");
		printf("			<div class=\"bigbox\" id=\"leftbb\">\n");
		printf("				<h1>go back</h1>\n");
		printf("			</div></a><br>\n");		
	}



	else{
	
		fgets(raw_input, len+1, stdin); //""
		
		int unencoded = unencode(raw_input+EXTRA, raw_input+len, id, pwd, rpwd, email);
/*
		printf("this is result from the unencode function: \n\n");
		printf("%s %s %s %s", id, pwd, rpwd, email);
		printf("<br><br>\n\n\n\n");*/
		//in case of incorrect format, create a warning page with a "back" button
		if (!strcmp(raw_input, "ID=&pwd=&rpwd=&email="))
		{
			printf("<h3>Please make sure your ID and password are at least 8 characters long.</h3>");
			printf("			<br><br><a href=\"http://www.cs.mcgill.ca/~syou3/Pollymorph/login.html\">\n");
			printf("			<div class=\"bigbox\" id=\"leftbb\">\n");
			printf("				<h1>go back</h1>\n");
			printf("			</div></a><br>\n");
		}
		else if (unencoded!=2){

			if (unencoded==0){
				printf("		<h3>Please do not use any spaces.<h3>\n");
			}

			else if (unencoded==1){
				printf("<h3>Please only use the alphabet, numbers, ., -, and/or _ in your ID.<h3>\n");
			}

			printf("			<br><br><a href=\"http://www.cs.mcgill.ca/~syou3/Pollymorph/login.html\">\n");
			printf("			<div class=\"bigbox\" id=\"leftbb\">\n");
			printf("				<h1>go back</h1>\n");
			printf("			</div></a><br>\n");

		}

		else
		{
			if (strcmp(pwd,rpwd)!=0){
				printf("Your passwords do not match.<br>\n");
				printf("			<br><br><a href=\"http://www.cs.mcgill.ca/~syou3/Pollymorph/login.html\">\n");
				printf("			<div class=\"bigbox\" id=\"leftbb\">\n");
				printf("				<h1>go back</h1>\n");
				printf("			</div></a><br>\n");				
			}
			else
			{				
				fprintf(in, "%s %s %s\n", id, pwd, email);
				printf("Your user name and password have been accepted.<br>\n");
			}
			
		}

	}
		




	printf("			<br><br><a href=\"http://www.cs.mcgill.ca/~cliu65/Pollymorph/welcome.html\">\n");
	printf("			<div class=\"bigbox\" id=\"leftbb\">\n");
	printf("				<h1>Return Home</h1>\n");
	printf("			</div></a>\n");
	printf("			<a href=\"http://cs.mcgill.ca/~syou3/Pollymorph/login.html\">\n");
	printf("			<div class=\"bigbox\" id=\"rightbb\">\n");
	printf("				<h1>Log In</h1>\n");
	printf("			</div></a>\n");
	printf("		</div></body>\n");

	fclose(in);

	return 0;}
