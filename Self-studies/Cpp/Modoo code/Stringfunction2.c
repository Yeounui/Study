#include <stdio.h>

int stradd(char *dest, char *src);

int main() {
    char str1[100] = "hello my name is ";
    char str2[] = "Psi";
    printf("합치기 이전 : %s \n", str1);
    stradd(str1, str2);
    printf("합친 이후 : %s \n", str1);
    return 0;
}
    
int stradd(char *dest, char *src) {
    while (*dest) {
        dest++;
    } // while 문 이후, 포인터 dest는 NULL 자리에 있음.
    
    while (*src) {
        *dest = *src;
        src++;
        dest++;
    }

    *dest = '\0'; // 마지막으로 dest 에 NULL 추가
    return 1;
}