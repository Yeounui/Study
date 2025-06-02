/* 변수의 이름 출력하기 */
#include <stdio.h>
#define PrintVariableName(var) printf(#var "\n"); // #뒤에 들어간 변수명을 string으로 바꿈.

int main(int argc, char **argv) {
    int a;
    PrintVariableName(a);
    return 0;
}
