/* 전역 변수 */
#include <stdio.h>
int global;
// global variable(전역 변수): 바깥에 정의; 프로그램 시작 시 만들어졌다가 프로그램 종료 시 파괴. 전역 변수 처음 정의 시 0.
// local variable(지역 변수): 안에 정의; 함수가 종료 될 때 파괴.
int function() {
    global++;
    return 0;
}
int main() {
    function();
    printf("%d \n", global);
    return 0;
}
