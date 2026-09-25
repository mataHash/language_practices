
#include <stdio.h>
#define MAXLINE 1000

	int max;
	char line[MAXLINE];
	char longest[MAXLINE];
int Getline(void){
	int c , i;
	extern char line[];
	for( i=0;
	     i< MAXLINE-1 && (c=getchar()) != EOF &&
	     c != '\n';
	     ++i){ 
		line[i]= c;
	}
	if(c == '\n'){
		line[i]=c;
		++i;
	}
	line[i]= '\0';
	return i;
}
void copy(void){
	int i = 0;
	extern char line[], longest[];
	while ((line[i] = longest[i]) != '\0'){
		++i;
	}

}

int main(){
	
	extern int max;
	extern char line[MAXLINE];
	extern char longest[MAXLINE];
	int len;
	while((len = Getline() > 0 )){
		if(len > max){
			max = len;
			copy();
		}
	}
	if(max > 0){
		printf("%s", longest);
	}


}
