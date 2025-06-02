/* #define
#define macrovariable value
전처리기 문들은 ; 를 붙이지 않음. 컴파일 이전에 정의*/

#include <stdio.h>
#define VAR 10 

int main() {
    char arr[VAR] = {"hi"};
    printf("%s\n", arr);
    return 0;
}