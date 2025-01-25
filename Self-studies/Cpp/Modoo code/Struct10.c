/*
구조체 변수를 정의하는 색다른 방법.
*/
#include <stdio.h>

struct obj {
    char name[20];
    int x, y;
}   Ball; // "struct obj Ball;"와 같음. obj 변수 Ball 정의.
char copy_str(char *dest, char *src);
int Print_Obj_Status(struct obj OBJ);

int main() {
    Ball.x = 3;
    Ball.y = 4;
    copy_str(Ball.name, "RED BALL");

    Print_Obj_Status(Ball);
    
    return 0;
}
int Print_Obj_Status(struct obj OBJ) { // 특정 구조체에 대한 명령어 정의. 마치 python의 상속 같이.
    printf("Location of %s \n", OBJ.name);
    printf("( %d , %d ) \n", OBJ.x, OBJ.y);
    return 0;
}
char copy_str(char *dest, char *src) {
    while (*src) {
        *dest = *src;
        src++;
        dest++;
    }

    *dest = '\0';

    return 1;
}
