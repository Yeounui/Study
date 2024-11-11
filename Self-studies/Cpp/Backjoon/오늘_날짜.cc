#include <iostream>
#include <ctime>

using namespace std;

int main() {
    char outcome[80];

    time_t currentSecond = time(0);   // 1970년 1월 1일로부터 얼마나 시간이 지났나 (초)
    tm* currentTime = gmtime(&currentSecond); // UTC 기준 시간으로 변환.

    strftime(outcome, 80, "%Y-%m-%d", currentTime); //시간을 원하는 형식으로 outcome에 담음.
    cout << outcome << endl;

	return 0;
}