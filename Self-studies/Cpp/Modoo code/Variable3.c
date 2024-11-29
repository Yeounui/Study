/* 변수 알아보기 3*/
#include <stdio.h>
    int main() {
    float a = 3.141592f;
    double b = 3.141592;
    /*
    float a = 3.141592 로 하면 이를 double 형으로 인식하여 문제가 생길 수 있음.
    float 형이라는 것을 확실히 표시해 주기 위해 f 를 끝에 붙이는 것.
    */
    printf("a : %f \n", a);
    printf("b : %f \n", b);
    return 0;
}