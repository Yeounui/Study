/* 상수 포인터? */
#include <stdio.h>
int main() {
int a;
int b;
const int* pa = &a; // 상수 포인터: int 형 변수를 가리키는 포인터를 다른 자료 형식으로 절대 바꾸지 말라
// *pa = 3; // 올바르지 않은 문장
pa = &b; // 올바른 문장
return 0;
}