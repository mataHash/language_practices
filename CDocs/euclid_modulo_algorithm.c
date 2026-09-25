
#include <stdio.h>
 int gcd(  int u,  int v){
	int R;
	R = u % v;
	if(R == 0){
		return R;
	}
	else{
	return gcd(v, R);
	}
}

int main(){
	 int x,y;
	while (scanf("%d %d", &x, &y) != EOF){
		if (x > 0 && y > 0){
			printf("%d %d %d\n", x, y, gcd(x,y));
			printf(" %d / %d \n", x / gcd(x,y) , y / gcd(x,y));
		}
	}
	printf("\n");
}
