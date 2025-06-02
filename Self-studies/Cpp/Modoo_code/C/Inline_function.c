/* 인라인 함수
   Inline function은 main에서 해당 함수를 메모리에서 호출하느라 시간을 소요하지 않고,
   바로 함수를 사용하기에 단순 계산 함수를 빨리 처리할 수 있음.
   컴파일러는 같은 이름의 함수를 호출하기 전에 인라인 함수가 더 효율적인지 판단 후 사용.
   아니라면 함수 호출. 그렇기에 전처리기보다 컴파일러에 권한을 더 줌.*/
#include <stdio.h>
__inline int square(int a) { return a * a; }

int main(int argc, char **argv) {
    printf("%d", square(3));
    return 0;
}