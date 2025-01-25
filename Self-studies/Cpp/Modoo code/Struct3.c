/* 구조체 포인터 */
#include <stdio.h>
struct test {
    int a, b;
};

int main() {
    struct test st;
    struct test *ptr;
    ptr = &st;
    (*ptr).a = 1; //혹은 ptr->a = 1;
    (*ptr).b = 2; //ptr->b = 2;
    printf("st 의 a 멤버 : %d \n", st.a);
    printf("st 의 b 멤버 : %d \n", st.b);
    return 0;
}