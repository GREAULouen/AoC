# include <regex>
# include <iostream>
# include <fstream>
# include <string>


int main(void) {
	std::ifstream file("input.txt");
	if (!file.is_open()) {
		std::cerr << "Could not open the file!" << std::endl;
		return 1;
	}

	std::string line;
	std::regex pattern(R"(mul\((\d{1,3}),(\d{1,3})\))");
	std::smatch match;
	int totalSum = 0;

	while (std::getline(file, line)) {
		std::sregex_iterator begin(line.begin(), line.end(), pattern), end;
		for (auto it = begin; it != end; ++it) {
			int num1 = std::stoi((*it)[1].str());
			int num2 = std::stoi((*it)[2].str());
			totalSum += num1 * num2;
		}
	}

	file.close();
	std::cout << "Total Sum: " << totalSum << std::endl;

	return 0;
}
