#include <stdio.h>

int main(){

	float celsius, fahr,
	lower, upper, step;

	lower = 0, upper = 300, step = 20;

	celsius = lower;
	printf("\n----celsius to fahrenheit table----\n");
	while(celsius <= upper){
		fahr = (9 * celsius / 5)+ 32;
		printf("%3.0f\t%6.2f\n",celsius, fahr);
		celsius += step;
	}

	return 0;
}
