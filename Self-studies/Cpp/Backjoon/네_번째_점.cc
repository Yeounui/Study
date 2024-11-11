#include <iostream>

using namespace std;


int main() {
    int coord_A[2], coord_B[2], coord_C[2], coord_D[2];
    cin >> coord_A[0] >> coord_A[1];
    cin >> coord_B[0] >> coord_B[1];
    cin >> coord_C[0] >> coord_C[1];
    
    for (int i = 0; i < 2; i++) {
        if (coord_A[i] == coord_B[i]) {
            coord_D[i] = coord_C[i];
        }
        else if (coord_A[i] == coord_C[i]) {
            coord_D[i] = coord_B[i];
        }
        else {
            coord_D[i] = coord_A[i];
        }
    }

    cout << coord_D[0] << ' ' << coord_D[1] << endl;
    return 0;
}
