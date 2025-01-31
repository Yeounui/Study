/* 메모리의 배치 모습 */
#include <stdio.h>

int global = 3;

int main() {
    int i;
    char *str = "Hello, Baby";
    char arr[20] = "WHATTHEHECK";
    printf("global : %p \n", &global);
    printf("i : %p \n", &i);
    printf("str : %p \n", str);
    printf("arr : %p \n", arr);
}

/*
On RAM: Stack (Local variable 위치) -> <- Heap | Code Segment(Global, Static variable 위치) | Read-Only Data (Constant, Literal 위치) | Data Segment
따라서 i && arr > global > *str
*/