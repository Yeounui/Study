/* 포인터 상수 */
#include <stdio.h>
int main() {
int a;
int b;
int* const pa = &a; // 포인터 상수: pa가 처음에 가리키는 a 변수의 주소값을 절대 건드릴 수 없음
*pa = 3; // 올바른 문장
// pa = &b; // 올바르지 않은 문장
return 0;
}