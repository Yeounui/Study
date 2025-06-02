#include <stdio.h>

int main() {
    int arr[6] = {1, 2, 3, 4, 5, 6};
    int* parr = arr;
    printf("Sizeof(arr) : %d \n", sizeof(arr));
    printf("Sizeof(parr) : %d \n", sizeof(parr));
    printf("a[3] : %d \n", arr[3]);
    printf("*(a+3) : %d \n", *(arr + 3));
    
}

/*
Sizeof(arr) : 24 # array 크기 4 byte * 6
Sizeof(parr) : 8 # 포인터 크기 8 byte
*/