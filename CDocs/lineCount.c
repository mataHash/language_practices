#include <stdio.h>

 int main(void) {
	int lc, c;
	while((c = getchar()) != EOF){
		if (c == '\n'){
			++lc;
		}
	}
	printf("%d\n", lc);
	return 0;
}
