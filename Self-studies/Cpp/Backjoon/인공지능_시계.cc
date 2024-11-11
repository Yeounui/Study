#include <iostream>

using namespace std;

int main() {
	int hour, minute, second, time;
    cin >> hour >> minute >> second >> time;

    second += time;
    minute += (second/60);
    hour += (minute/60);

    second %= 60;
    minute %= 60;
    hour %= 24;

    cout << hour<< " " << minute << " " << second << endl;

	return 0;
}