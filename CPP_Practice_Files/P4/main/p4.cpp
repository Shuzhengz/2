#include <iostream>
using namespace std;

int a;

class output {
public:
	output(int out) {
	*out_ = out;
	}

	int *outp() {
		return out_;
	}

private:
	int *out_ = &a;
};

class input {
public:
	input(int in){
	*in_ = in;
	}

	int *intp(){
		return in_;
	}

private:
	int *in_ = &a;
};

int main() {
	cout << "Input a number: " << endl;
	int h;
	cin >> h;
	input x (h);
	output y = output (a);
	cout << *(y.outp()) << endl;
	return 0;
}