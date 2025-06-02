/* 과연? */
#include <stdio.h>
int main() {
    int arr[3] = {1, 2, 3};
    printf("arr 의 정체 : %p \n", arr); // array 주소값은 decorator 없음.
    printf("arr[0] 의 주소값 : %p \n", &arr[0]);
    return 0;
}
/*
arr 의 정체 : 0x7fffffffdb0c 
arr[0] 의 주소값 : 0x7fffffffdb0c # 시작점이 첫번째 주소와 같음
*/
