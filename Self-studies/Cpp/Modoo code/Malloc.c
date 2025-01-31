#include <stdio.h>
#include <stdlib.h>
int main(int argc, char **argv) {
    int SizeOfArray;
    int *arr;

    printf("만들고 싶은 배열의 원소의 수 : ");
    scanf("%d", &SizeOfArray);

    arr = (int *)malloc(sizeof(int) * SizeOfArray); // int arr[SizeOfArray] 와 동일한 작업을 한 크기의 배열 생성
    /*malloc: memory allocation
    <stdlib.h>에 정의되어 있음. Output은 void형, 그러므로 (int *)로 형 변환.
    malloc 함수를 통해 메모리 Heap 부분(String9.c 참조)을 직접 할당 혹은 해제 가능.*/
    free(arr);
    /*free
    다 쓰고 난 후 메모리를 다시 컴퓨터에게 반환.
    메모리 할당을 해제 안 할 경우 memory leak 발생.*/
    return 0;
}