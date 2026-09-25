#include<stdio.h>

int main(){

	int character, index, nwhites, nother = 0;
	int ndigit[10];

	for(index = 0; index < 10; ++index){
		ndigit[index] = 0;
	}
	while ((character = getchar()) != EOF){
		if(character >= '0' && character <= '9'){
			++ndigit[character - '0'];	
		}
		else if (character == ' ' || character == '\t' || character == '\n') {
			++nwhites;
		}
		else {
			++nother;
		}
	
	}
	printf("digits =");
	for(index = 0; index < 10; ++index){
		printf(" %d", ndigit[index]);
	}
	printf(", white space = %d, other = %d\n", nwhites, nother);
	return 0;
}
