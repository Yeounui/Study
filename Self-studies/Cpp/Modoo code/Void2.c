/* 임의의 주소값 p 로 부터 byte 만큼 읽은 함수*/
#include <stdio.h>

int read_char(void *p, int byte);

int main() {
    int arr[1] = {0x12345678};

    printf("%x \n", arr[0]);
    read_char(arr, 4);
}

int read_char(void *p, int byte) {
    do {
    printf("%x \n", *(char *)p);
    byte--;
    // 리틀 엔디안 (Struct11.c 참조): 낮은 주소 값(78)부터 상위 비트 할당.
    // x0(16진수)에서 78|56|34|12 할당.

    p = (char *)p + 1;
    } while (p && byte);

    return 0;
}