/* 인자를 가지는 메인 함수 */
#include <stdio.h>
    int main(int argc, char **argv) { // **argv: Pointer of pointer of char type
    int i;

    printf("받은 인자의 개수 : %d \n", argc);
    for (i = 0; i < argc; i++) {
    printf("이 프로그램이 받은 인자 : %s \n", argv[i]);
    }

    return 0;
}
/*
./Arguments 1 2 3
받은 인자의 개수 : 4 
이 프로그램이 받은 인자 : ./Arguments 
이 프로그램이 받은 인자 : 1 
이 프로그램이 받은 인자 : 2 
이 프로그램이 받은 인자 : 3 
argv[]
*/