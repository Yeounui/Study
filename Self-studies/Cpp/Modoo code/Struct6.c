/*
구조체 포인터 연습
*/
#include <stdio.h>

int add_one(int *a);

struct TEST {
    int c;
};

int main() {
    struct TEST t;
    struct TEST *pt = &t;
    /* pt 가 가리키는 구조체 변수의 c 멤버의 값을 0 으로 한다*/
    pt->c = 0;
    /*
    add_one 함수의 인자에 t 구조체 변수의 멤버 c 의 주소값을
    전달하고 있다.
    */
    add_one(&t.c);
    printf("t.c : %d \n", t.c);
    /*
    add_one 함수의 인자에 pt 가 가리키는 구조체 변수의 멤버 c
    의 주소값을 전달하고 있다.
    */
    add_one(&pt->c);
    printf("t.c : %d \n", t.c);
    return 0;
}

int add_one(int *a) {
    *a += 1;
    return 0;
}