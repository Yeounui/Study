/* 포인터도 변수이다 */
#include <stdio.h>

int main() {
    int a;
    int b;
    int *p; //p는 포인터

    p = &a; //p는 int a의 주소값과 같다.
    *p = 2; //p의
    p = &b;
    *p = 4;
    
    printf("a : %d \n", a);
    printf("b : %d \n", b);
    
    return 0;
}

/*
a : 2
b : 4
*/

