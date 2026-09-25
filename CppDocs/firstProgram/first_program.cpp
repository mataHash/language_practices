#include <iostream>

int main()
{
	std::cout << "Enter an Integer: " ;
	int number {};
	std::cin >> number;
	std::cout << " Double "<< number << " is : "<< number * 2 <<'\n';
	std::cout << " triple "<< number << " is : "<< number * 3 <<'\n';
	return 0;
}
