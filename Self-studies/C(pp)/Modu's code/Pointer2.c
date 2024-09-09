/* * 연산자의 이용 */
#include <stdio.h>
int main() {
    int *p;
    int a;
    p = &a;
    a = 2;
    printf("a 의 값 : %d \n", a);
    printf("*p 의 값 : %d \n", *p);
    return 0;
}

/*
a 의 값 : 2
*p 의 값 : 2
*/