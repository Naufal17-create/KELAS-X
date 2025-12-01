#include <iostream>
using namespace std;

int main() {
    int t;

    cout << "Masukkan tinggi segitiga : ";
    cin >> t;

    // ============================
    // SEGITIGA SIKU-SIKU KANAN ATAS
    // ============================
    cout << "\n=== Segitiga Siku-Siku Kanan Atas ===\n";

    for(int i = 1; i <= t; i++) {
        for(int j = 1; j < i; j++) {
            cout << " ";
        }
        for(int k = i; k <= t; k++) {
            cout << "*";
        }
        cout << endl;
    }
    return 0;
}
