#include <cmath>
#include <iostream>
#include <fstream>

using namespace std;
using ld = long double;
using ll = long long;

const ld delta_t = 0.1;

const ld GM = 65138397520;
const ld MR = 200000;

int main() {
    const char* filename = "math_model_data.txt";
    ofstream outputFile(filename);

    ld speed, height, time, acceleration;
    cout << "Начальное значение скорости = ";
    cin >> speed;
    cout << "Начальное значение высоты = ";
    cin >> height;
    time = 0;

    outputFile << "Высоты, Вертикальная скорость, Время" << endl;
    outputFile.precision(20);
    outputFile << fixed;
    outputFile << height << ", " << speed << ", " << time << endl;

    while (height > 20000) {
        acceleration = GM / pow(MR + height, 2);
        height -= speed * delta_t;
        speed += acceleration * delta_t;
        time += delta_t;
        outputFile << height << ", " << speed << ", " << time << endl;
    }
}