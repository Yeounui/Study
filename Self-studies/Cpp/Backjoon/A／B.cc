#include <stdio.h>
 
int main(int argc, char const *argv[]) { // char const *argv[]: 명령 줄 인수를 포인터 배열로 나타낸 거 (const는 불변) ex: 프로그램 input1 input2; 
										 // argv[0]는 프로그램 / int argc : 명령줄 인수의 수 ex: 여기서는 3
    double a;
    double b;
 
    scanf("%lf %lf", &a, &b);	// double 입력은 %lf, &은 변수의 주소를 나타냄
 
    /*
     lf 출력은 소수점 6자리까지 기본 출력
     오차범위가 10^-9 이하 시 %.10lf.
    */
    printf("%.10lf", a / b);
    
    return 0;
}

/*
#include <iostream>
 
using namespace std;
int main(int argc, char const *argv[]) {
 
    double a, b;
    cin >> a >> b;
 
    cout.precision(12);
    cout << fixed;
    cout << a / b;
    return 0;
}
*/