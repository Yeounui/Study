/* printf 형식 */
#include <stdio.h>

int main() {
    float a = 3.141592f;
    double b = 3.141592;
    int c = 123;
    printf("a : %.2f \n", a); //소수점 이하 둘째 자리 까지만 표시
    printf("c : %5d \n", c); //숫자의 자리 칸를 5자리로 맞추라
    printf("b : %6.3f \n", b); //전체 자리 칸을 6자리로 맞추되 반드시 소수점 이하 셋째 자리 까지만 표시
    return 0;
}
