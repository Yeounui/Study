/* 구조체의 도입*/
#include <stdio.h>

struct Human {
    int age; /* 나이 */
    int height; /* 키 */
    int weight; /* 몸무게 */
};

int main() {
    struct Human Psi;
    Psi.age = 99;
    Psi.height = 185;
    Psi.weight = 80;
    printf("Psi 에 대한 정보 \n");
    printf("나이 : %d \n", Psi.age);
    printf("키 : %d \n", Psi.height);
    printf("몸무게 : %d \n", Psi.weight);
    return 0;
}