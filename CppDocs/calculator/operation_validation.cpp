#include "calculator.h"
double validation(char operation, double num1, double num2){
switch(operation){
		case '+':
			return calculator::sum(num1, num2);
			break;
		case '-':
			return calculator::sub(num1, num2);
			break;
		case '*':
			return calculator::prod(num1, num2);
			break;
		case '/':
			return calculator::divide(num1, num2);
			break;
		default:
			return -1;
	}
}
