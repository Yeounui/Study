#include <stdio.h>
#pragma pack(1) // 전처리기 명령엔 ; 안 붙임.
struct Weird {
    char arr[2]; // 1byte * 2
    int i; // 4 byte.
};
/*
컴퓨터에서 데이터를 보관 시 4의 배수가 처리시 용이.
그렇기에 위 Weird struct 역시 4 의 배수에 맞추려 2 바이트를 추가함. (더블 워드 경계에 놓임.)
이 문제가 중요하게 여겨지는 부분은 하드웨어 간의 통신.
예로, SCSI 인터페이스는 PC에서 주변 기기에 연결하기 위한 통신 방식으로
SCSI 장치들에게 읽기 명령을 내리기 위해 6 바이트의 명령어를 전송.
이 6 바이트의 명령어의 구조는 꽤 복잡해서 흔히 구조체로 많이 이용,
pragma 설정 없다면 구조체의 크기가 8 바이트로 설정되어 오류 발생.
구조체를 더블 워드 경계에 놓이지 않도록 pragma 키워드를 이용; 재설정 시 pack(4) */
int main() {
    struct Weird a;
    printf("size of a : %d \n", sizeof(a)); //6이 나와야 하지만 8이 출력.
    return 0;
}