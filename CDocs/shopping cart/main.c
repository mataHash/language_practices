#include <stdio.h>
#include <string.h>

int main(){

	char item[50]= "";
	float price = 0.0f;
	int quantity = 0;
	char currency = '$';
	float total = 0.0f;

	printf("what item would you like to buy: ");
	fgets(item, sizeof(item), stdin);
	item[strcspn(item, "\n")] = '\0';

	printf("what is the price for each: ");
	scanf("%f", &price);

	printf("How many would you like to buy: ");
	scanf("%d", &quantity);
	total = price * quantity;

	printf("You have bought %d %ss\n", quantity, item);
	printf("The total is: %c%.2f\n", currency, total);
	return 0;
}
