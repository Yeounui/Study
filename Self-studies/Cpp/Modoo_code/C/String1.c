/* 널 뽀개기 */
#include <stdio.h>
int main() {
    char null_1 = '\0'; // 이 3 개는 모두 동일하다
    char null_2 = 0;
    char null_3 = (char)NULL; // 모두 대문자로 써야 한다
    char not_null = '0';
    printf("NULL 의 정수(아스키)값 : %d, %d, %d \n", null_1, null_2, null_3);
    printf("'0' 의 정수(아스키)값 : %d \n", not_null);
    return 0;
}

/*
NULL 의 정수(아스키)값 : 0, 0, 0 
'0' 의 정수(아스키)값 : 48 
*/