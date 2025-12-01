#include <iostream>
using namespace std;

int main() {
    int tinggi;

    cout << "Masukkan tinggi segitiga: ";
    cin >> tinggi;

    cout << "\n=== Segitiga Sama Kaki ===" << endl;

    for(int i = 1; i <= tinggi; i++) {

        // Spasi di kiri (supaya segitiga berbentuk sama kaki)
        for(int s = 1; s <= tinggi - i; s++) {
            cout << " ";
        }

        // Bintang (jumlahnya 2*i-1)
        for(int b = 1; b <= (2 * i - 1); b++) {
            cout << "*";
        }

        cout << endl;
    }

    return 0;
}
