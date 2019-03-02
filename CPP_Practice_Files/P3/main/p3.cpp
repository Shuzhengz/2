#include <iostream>

class Data {
	public:
		Data(int amount, int size, int weight) {
			amount_ = amount;
			size_ = size;
			weight_ = weight;
		}
		int* reamountP() {
			return &amount_;
		}
		int* resizeP() {
			return &size_;
		}
		int* reweightP() {
			return &weight_;
		}

	private:
		int amount_;
		int size_;
		int weight_;
};

int main() {
	Data x (0, 0, 0);
	int *amountP = x.reamountP();
	*amountP = 1;
	std::cout << *amountP << std::endl;
	int * sizeP = x.resizeP();
	*sizeP = 2;
	std::cout << *sizeP << std::endl;
	int *weightP = x.reweightP();
	*weightP = 3;
	std::cout << *weightP << std::endl;
}