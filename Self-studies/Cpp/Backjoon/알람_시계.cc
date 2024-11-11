#include <iostream>

using namespace std;

int main() {
    int time[2];
    cin >> time[0] >> time[1];
    
    time[1] -= 45;
    if (time[1] < 0) {
        time[1] += 60;
        time[0]--;
        if (time[0] < 0) {
            time[0] += 24;
        }
    }
    cout << time[0] << " " << time[1] << endl;
	return 0;
}