#include <stdio.h>
#define LOWER 0
#define UPPER 300
#define STEP 20
int main(){
	
	int fahr;
	for(fahr = 0; fahr <= 300; fahr += STEP){
		printf("%3.0d\t%6.1d\n", fahr,(5*(fahr - 32)/9));
}
	return 0;
}
