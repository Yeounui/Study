/* 구조체를 리턴하는 함수 */
#include <stdio.h>
struct AA function(int j);
struct AA {
    int i;
};
int main() {
    struct AA a;
    a = function(10);
    printf("a.i : %d \n", a.i);
    return 0;
}
struct AA function(int j) { // 특정 구조체에 대한 함수 정의.
    struct AA A;
    A.i = j;
    return A;
}
