/* 포인터의 포인터 */
#include <stdio.h>

int main() {
    int a;
    int *pa;
    int **ppa;
    pa = &a;
    ppa = &pa;
    a = 3;
    printf("a : %d // *pa : %d // **ppa : %d \n", a, *pa, **ppa);
    printf("&a : %p // pa : %p // *ppa : %p \n", &a, pa, *ppa);
    printf("&pa : %p // ppa : %p \n", &pa, ppa);
    return 0;
}

/*
a : 3 // *pa : 3 // **ppa : 3 
&a : 0x7fffffffdb04 // pa : 0x7fffffffdb04 // *ppa : 0x7fffffffdb04 
&pa : 0x7fffffffdb08 // ppa : 0x7fffffffdb08 
*/