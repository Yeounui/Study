/* 포인터도 변수이다 */
#include <stdio.h>

int main() {
    int a;
    int b;
    int *p;

    p = &a;
    *p = 2;
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

