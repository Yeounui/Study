/*int copy_str(char *dest, char *src);
src 의 문자열을 dest 로 복사한다. 단, dest 의 크기가 반드시 src 보다 커야 한다.*/
/* copy_str 사용 예제 */
#include <stdio.h>

int copy_str(char *src, char*dest);

int main() {
    char str1[] = "hello";
    char str2[] = "hi";

    printf("복사 이전 : %s \n", str1);

    copy_str(str1, str2);

    printf("복사 이후 : %s \n", str1);
    
    return 0;
}

int copy_str(char *dest, char *src) {
    while(*src) {
        *dest = *src;
        src++;
        dest++;
    }

    *dest = '\0';

    return 1;
}