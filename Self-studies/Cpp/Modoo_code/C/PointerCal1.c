/* 포인터의 덧셈 */
#include <stdio.h>

int main() {
    int a;
    char b;
    double c;
    int* pa = &a;
    char* pb = &b;
    double* pc = &c;
    printf("pa 의 값 : %p \n", pa);
    printf("(pa + 1) 의 값 : %p \n", pa + 1);
    printf("pb 의 값 : %p \n", pb);
    printf("(pb + 1) 의 값 : %p \n", pb + 1);
    printf("pc 의 값 : %p \n", pc);
    printf("(pc + 1) 의 값 : %p \n", pc + 1);
    return 0;
}

/*
pa 의 값 : 0x7fffffffdb04 
(pa + 1) 의 값 : 0x7fffffffdb08 # int는 메모리를 4바이트씩 할당 
pb 의 값 : 0x7fffffffdb03 
(pb + 1) 의 값 : 0x7fffffffdb04 # char은 메모리를 1바이트씩 할당 
pc 의 값 : 0x7fffffffdb08 
(pc + 1) 의 값 : 0x7fffffffdb10 # double은 메모리를 8바이트씩 할당
*/