#include <iostream>
#include <string>
#include <ctime>
#include <vector>
#include <algorithm>
#include <windows.h>

using namespace std;

vector<string> getCombinations(int k, const string &alf) {
    vector<string> combinations;
    string combination(k, alf[0]);
    while (true) {
        combinations.push_back(combination);
        int i = k - 1;
        while (i >= 0 && combination[i] == alf[alf.size() - 1]) {
            --i;
        }
        if (i == -1) break;
        combination[i] = alf[alf.find(combination[i]) + 1];
        for (int j = i + 1; j < k; ++j) {
            combination[j] = alf[0];
        }
    }
    return combinations;
}

double bruteForce(const string &n) {
    string alf = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    string result = "";
    int k = 0;


    clock_t start = clock();


    while (result != n) {
        k++;
        vector<string> combinations = getCombinations(k, alf);
        for (const auto &a : combinations) {
            result = a;
            if (result == n) {
                break;
            }
        }
    }


    clock_t end = clock();
    double duration = double(end - start) / CLOCKS_PER_SEC;

    return duration;
}

extern "C" {
    double print_string(const char* str) {
        SetConsoleOutputCP(CP_UTF8);

        double duration = bruteForce(str);

        return duration;
    }
}