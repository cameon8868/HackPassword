// Сделано ИИ
#include <iostream>
#include <string>
#include <ctime>
#include <vector>
#include <algorithm>

using namespace std;

// Функция для генерации всех возможных комбинаций длины k с символами из 'alf'
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

// Функция для выполнения brute-force поиска
string bruteForce(const string &n) {
    string alf = "1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz";
    string result = "";
    int k = 0;

    // Засекаем время начала
    clock_t start = clock();

    // Ищем строку методом brute-force
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

    // Засекаем время окончания
    clock_t end = clock();
    double duration = double(end - start) / CLOCKS_PER_SEC;

    // Выводим время выполнения
    cout << "Время выполнения: " << duration << " секунд." << endl;
    
    return result;
}

int main() {
    string input;
    cout << "Введите пароль: ";
    cin >> input;

    string result = bruteForce(input);
    cout << "Результат: " << result << endl;

    return 0;
}