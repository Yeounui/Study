#include <iostream>

using namespace std;

int main() {
	int hour, minute, time;
    cin >> hour >> minute >> time;

    minute += time;
    hour = (hour + (minute/60)) % 24;
    minute %= 60
    
    cout << hour<< " " << minute << endl;

	return 0;
}