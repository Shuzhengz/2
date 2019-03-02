#include <iostream>

int main() {
	std::cout << "What is your height (in cm)? " << std::endl;                     // asks what the height is
	int h;
	std::cin >> h;
	std::cout << "What is your weight (in kg)? " << std::endl;                     // asks what the weight is
	int w;
	std::cin >> w;
	std::cout <<"Your BMI is: " << h / 100 / w / w << "/sqrmeters" << std::endl;   // prints and calculates
	return 0;                                                                      // the end
}
