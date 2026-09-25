#include <stdio.h>
#include <stdbool.h>
bool iswhitespace(char character){
bool is = (character == ' ' || character == '\n' || character == '\t') ? true : false;
 return is;
}
int main(){

	int character, newLine, newWord, newCharacter;
	bool state = false;
	while ( (character = getchar()) != EOF){
		if(character == '\n')
			++newLine;
		if (iswhitespace(character))
			state = false;
		else if (state==false){
			state = true;
			++newWord;
			printf("%s\n", (char)character);
		}
	}
	return 0;
}
