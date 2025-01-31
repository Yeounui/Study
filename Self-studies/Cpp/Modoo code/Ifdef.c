/* ifdef
#ifdef Macro_variable
(매크로 이름)이 정의되었다면 이 부분이 코드에 포함되고 그렇지 않다면 코드에 포함되지 않음.
#endif */
#include <stdio.h>
#define A // or B

int main() {
#ifdef A
printf("AAAA \n");
#endif

#ifdef B
printf("BBBB \n");
#endif

    return 0;
}