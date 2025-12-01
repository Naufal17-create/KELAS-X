#include <iostream>
using namespace std;

int main() {
    int t;

    cout << "Masukkan tinggi segitiga: ";
    cin >> t;

    cout << "\n=== Segitiga Siku-Siku Kiri Atas ===" << endl;

    for(int i = t; i >= 1; i--) {
        for(int j = 1; j <= i; j++) {
            cout << "*";
        }
        cout << endl;
    }

    return 0;
}
