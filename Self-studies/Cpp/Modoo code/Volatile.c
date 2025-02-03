#include <stdio.h>

typedef struct SENSOR {
/* 감지 시 1, 아닐 경우 0*/
    int sensor_flag;
    int data;
    } SENSOR;
int main() {
    volatile SENSOR *sensor;
    /* 값이 감지되지 않는 동안 계속 무한 루프를 돔.
       Complier가 "sensor->sensor_flag"을 최적화하면서
       if (!(sensor->sensor_flag)) { while (1) { } }
       이렇게 코드를 바꿔버림. 그렇기에 volatile로 최적화를 방지.
       volatile 키워드를 사용하는 경우: 외부 하드웨어와 통신할 때 사용.*/
    while (!(sensor->sensor_flag)) { 
    }
    printf("Data : %d \n", sensor->data);
}
