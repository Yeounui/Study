#include <stdio.h>

int main() {
    void *a; // 오로지 주소값만 할당받음.
    double b = 123.3;

    a = &b;
    printf("%lf", *(double *)a);

    return 0;
}