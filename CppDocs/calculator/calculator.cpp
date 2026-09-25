#include "calculator.h"
	double calculator::sum(double num1, double num2){
		return num1 + num2;
	}
	double calculator::sub(double num1, double num2){
		return num1 - num2;
	}

	double calculator::prod(double num1, double num2){
		return num1 * num2;
	}

	double calculator::divide(double num1, double num2){
		if (num2 == 0){
			return -1;
		}
		else {
			return num1 / num2;
		}
	}
