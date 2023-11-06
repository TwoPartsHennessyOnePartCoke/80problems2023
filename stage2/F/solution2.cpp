// WA, Тест 12: неверный ответ

#include <iostream>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;

    int a1 = 1;
    int top = floor(n / 2);
    while (true) {
        int c = a1 - a1 * a1;
        int an_approx = floor(sqrt(2 * n + a1 * a1 - a1));
        for (int i = an_approx; i < an_approx + ceil(sqrt(an_approx)) + 1; i++) {
            if (2 * n == i * i + i + c) {
                cout << i - a1 + 1 << endl;
                return 0;
            }
        }
        a1 += 1;
    }

    return 0;
}
