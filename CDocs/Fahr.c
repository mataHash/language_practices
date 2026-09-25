#include <stdio.h>

double celsiusToFahr(double celsius){

	return 5 * (celsius + 32) / 9;

}
int main(){

	double celsius = 0;
	while(celsius <= 300){
		printf("%3.1f\t%6.2f\n", celsius, celsiusToFahr(celsius));
		celsius += 20;
	}
	return 0;
}
