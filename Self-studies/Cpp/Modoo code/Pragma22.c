/* 이상한 test.c*/
#include <stdio.h>
#include "Pragma21.c"
int main() {
    struct Weird a;
    a.i = 3;
    printf("Weird 구조체의 a.i : %d \n", a.i);
    return 0;
}