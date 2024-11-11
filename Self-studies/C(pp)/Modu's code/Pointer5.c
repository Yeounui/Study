/* 상수 포인터? */
#include <stdio.h>
int main() {
int a;
int b;
int* const pa = &a; //pa가 처음에 가리키는 것 (a) 말고 다른 것은 절대로 건드릴 수 없음
*pa = 3; // 올바른 문장
// pa = &b; // 올바르지 않은 문장
return 0;
}