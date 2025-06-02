/* 포인터의 시작 */
#include <stdio.h>
int main() {
    int *p; // p는 정수형의 값이 들어가 있는 주소값을 나타내는 포인터임을 정의.
    int a;
    p = &a; // a의 주소값을 p에 할당.
    printf("포인터 p 에 들어 있는 값 : %p \n", p);
    printf("int 변수 a 가 저장된 주소 : %p \n", &a);
    return 0;
}

/*
포인터 p 에 들어 있는 값 : 0x7fff894c8b3c
int 변수 a 가 저장된 주소 : 0x7fff894c8b3c
*/