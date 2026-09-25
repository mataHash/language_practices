#include <stdio.h>

int main(){
	int a = 10;
	int* b = &a;

	printf("%p\n", b);
	printf("size of integer is %zu bytes\n", sizeof(int));
	printf("%p\n", b+1);

}
