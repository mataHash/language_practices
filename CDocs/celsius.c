#include <stdio.h>
// this program converts fahrenheit temps to celsius by making a list
int main (){
	
	float fahr, celsius,
	lower, upper, step;

	lower = 0, upper = 300, step = 20;
	fahr = lower;
	printf("\n----Farenheint to celsius Table(0-300)----\n");
	while(fahr <= upper){
		celsius = 5 * (fahr - 32) / 9;
		printf("%3.0f\t%6.1f\n", fahr, celsius);
		fahr += step;
	}
return 0;
}
