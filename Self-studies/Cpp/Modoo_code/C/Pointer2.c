/* * 연산자의 이용 */
#include <stdio.h>
int main() {
    int *p;
    int a;
    p = &a;
    a = 2;
    printf("a 의 값 : %d \n", a);
    printf("*p 의 값 : %d \n", *p); // 여기서 *p의 p는 메모리 주소를 나타내고 *은 메모리 주소에 있는 값을 가져오도록 함.
    return 0;
}

/*
a 의 값 : 2
*p 의 값 : 2
=의 왼쪽   *p: 주소값을 받아들이는 변수 정의.
=의 오른쪽 *p: p에 저장된 주소값을 참고하여 저장되어있는 값을 불러내어 변수에 할당.
=의 오른쪽 &a: a의 주소값을 불러내어 변수에 할당.
*/