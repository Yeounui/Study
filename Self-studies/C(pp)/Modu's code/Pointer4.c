/* 상수 포인터? */
#include <stdio.h>
int main() {
int a;
int b;
const int* pa = &a; // int 형 변수를 가리키는데 그 값을 절대로 바꾸지 말라
// *pa = 3; // 올바르지 않은 문장
pa = &b; // 올바른 문장
return 0;
}