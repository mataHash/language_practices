#include <iostream> 
#include "operation_validation.h"
int main(){

	// Variables used
	double num1{};
	double num2{};
	char ope{};

		// greeting
	std::cout << "Welcome to the mini calculator!"<<'\n';
		// first number
	std::cout << "Enter a number: ";
	std::cin >> num1;
	std::cout << "Entered number: " << num1 << '\n';

		// second number
	std::cout << "Enter another number: ";
	std::cin >> num2;
	std::cout << "Entered number: " << num2 << '\n';

		// operation selection
	std::cout << "Enter an operator: " << '\n';
	std::cout << "Accepted values:"<< '\n' << "addition: +" << '\n' << "substraction: -" << '\n' << "product: *" << '\n' << "division: /" << '\n';
	std::cout <<"Enter an operator: ";
	std::cin >> ope;
	std::cout << "Entered operation: " << ope << '\n';

		//  calling function validation and operation
	double calculation {validation(ope,num1,num2)};
	std::cout << "The result is: " << calculation << '\n';
	std::cout << "end of operation"<< '\n';

	return 0;
}
