/* 드디어! 배우는 배열의 포인터 */
#include <stdio.h>
int main() {
    int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
    int(*parr)[3]; // 괄호를 꼭 붙이세요
    parr = arr; // parr 이 arr 을 가리키게 한다.
    printf("parr[1][2] : %d , arr[1][2] : %d \n", parr[1][2], arr[1][2]);
    return 0;
}

/*
parr[1][2] : 6 , arr[1][2] : 6 
*/