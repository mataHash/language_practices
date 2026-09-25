#include <stdio.h>

int main(){

	int x= 1, y=2, z[10];
	int *ip;
	ip = &x;
	printf("%p\n",(void *)ip);

}
