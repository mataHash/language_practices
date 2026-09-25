#include <stdio.h>
int main(){
	int a;
	int *p;
	p = &a;
	a = 10;
	printf("%d\n",a);

	*p = 12;
	printf("%d\n",a);


return 0;
}
