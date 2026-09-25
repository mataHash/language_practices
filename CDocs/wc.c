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
		++newCharacter;
		if(character == '\n')
			++newLine;
		if (iswhitespace(character))
			state = false;
		else if (state==false){
			state = true;
			++newWord;
		}
	}
	printf("%d %d %d\n", newLine, newWord, newCharacter);
	return 0;
}
