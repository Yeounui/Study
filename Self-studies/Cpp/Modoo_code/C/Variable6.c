/* 정적 변수의 활용 */
#include <stdio.h>
int function() {
    static int how_many_called = 0; // static variable은 선언된 범위를 벗어나더라도 절대로 파괴되지 않음.
    
    how_many_called++;
    printf("function called : %d \n", how_many_called);
    return 0;
}
int function2() {
    static int how_many_called = 0;
    
    how_many_called++;
    printf("function 2 called : %d \n", how_many_called);
    return 0;
}
int main() {
    function();
    function2();
    function();
    function2();
    function2();
    function2();
    function();
    function();
    function2();
    return 0;
}
