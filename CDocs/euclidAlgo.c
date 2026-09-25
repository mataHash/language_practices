#include <stdio.h>
unsigned int gcd( unsigned int u, unsigned int v){

	while (u != 0) {
		if (u < v) {
			u = u ^ v;
			v = u ^ v;
			u = u ^ v;
		}
		else {
			u -=v;
		}
	}
	return v;
}

int main(){
	unsigned int x,y;
	while (scanf("%d %d", &x, &y) != EOF){
		if (x > 0 && y > 0){
			printf("%d %d %d\n", x, y, gcd(x,y));
			printf(" %d / %d \n", x / gcd(x,y) , y / gcd(x,y));
		}
	}
	printf("\n");
}
