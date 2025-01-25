/* 헷갈림 */
#include <stdio.h>
struct TEST {
    int c;
    int *pointer;
    };
    
int main() {
    struct TEST t;
    struct TEST *pt = &t;
    int i = 0;
    /* t 의 멤버 pointer 는 i 를 가리키게 된다*/
    t.pointer = &i;
    /* t 의 멤버 pointer 가 가리키는 변수의 값을 3 으로 만든다*/
    *t.pointer = 3;
    printf("i : %d \n", i);
    /*
    -> 가 * 보다 우선순위가 높으므로 먼저 해석하게 된다.
    즉, "(pt 가 가리키는 구조체 변수의 pointer 멤버) 가 가리키는 변수의 값을 4 로 바꾼다." 라는 뜻이다
    */
    *pt->pointer = 4;
    printf("i : %d \n", i);
    return 0;
}
