#include <stdio.h>
#define MAX_WIDTH 8

int main(){
	int Char, spaces_needed, column = 0;
	while ( (Char = getchar() ) != EOF){
		if (Char == '\t'){
			spaces_needed = MAX_WIDTH - column % MAX_WIDTH;
			while (spaces_needed > 0){
				putchar(' ');
				column++;
				--spaces_needed;
			}
		}
		else {
			putchar(Char);

			if(Char == '\n'){
				column = 0;
			}
			else{
				column++;
			}
		}

	}
	return 0;
}
