/* 라디안에서 도로 바꾸기*/
#include <stdio.h>
#define RADTODEG(x) ((x) * 57.295) // "1 / RADTODEG(5)"의 경우 계산이 달라지기 때문에 괄호를 붙여줘야함.

int main(int argc, char **argv) {
    printf("5 rad 는 : %f 도", RADTODEG(5));
    return 0;
}
