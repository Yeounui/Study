/* ## 의 사용 */
#include <stdio.h>
#define AddName(x, y) x##y //## 앞 뒤의 변수명을 합쳐버림.

int main(int argc, char **argv) {
    int AddName(a, b);
    ab = 3;
    printf("%d \n", ab);
    return 0;
}