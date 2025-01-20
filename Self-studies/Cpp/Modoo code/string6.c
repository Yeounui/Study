/* 문자열 입력 */
#include <stdio.h>
int main() {
    char *str = "abcdefghi"; // str은 포인터, *str은 값이므로, *str의 값을 정의해줘서 str 크기가 정해짐.
    char c_str[]={"abcdefghi"};
    printf("%s", str); /* 하면 잘 출력된다.*/
    return 0;
}