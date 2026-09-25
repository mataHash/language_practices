#include <iostream>
#include <string>

int main(){
	
	std::cout << "Enter your Full Name:"<<'\n';
	std::string name{};
	std::getline(std::cin >> std::ws, name);

	std::cout << "What's your favorite color?"<<'\n';
	std::string color{};
	std::getline(std::cin >> std::ws, color);

	std::cout << "Your name is "<< name << " and your favorite color is "<< color <<'\n';

}
