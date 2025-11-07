// Task 1.cpp : This file contains the 'main' function. Program execution begins and ends there.
//

#include <iostream>
#include <fstream>

int main()
{
	std::cout << "Hello world";

	std::ofstream MyFile("hello.txt");

	MyFile << "Hello World";

	//MyFile.close();
}

