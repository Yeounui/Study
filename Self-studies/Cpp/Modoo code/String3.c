/* 포인터 간단 복습 */
#include <stdio.h>
int main() {
    char word[30] = {"long sentence"}; // 다문자는 ""
    char *str = word;
    printf("조작 이전 : %s \n", str);
    word[0] = 'a'; // 단문자는 ''
    word[1] = 'b';
    word[2] = 'c';
    word[3] = 'd';
    printf("조작 이후 : %s \n", str);
}

/*
조작 이전 : long sentence 
조작 이후 : abcd sentence 
*/