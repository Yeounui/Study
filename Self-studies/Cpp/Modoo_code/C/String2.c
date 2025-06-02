/* 문자열의 시작 */
#include <stdio.h>
int main() {
    char sentence_1[4] = {'P', 's', 'i', '\0'};
    char sentence_2[4] = {'P', 's', 'i', 0};
    char sentence_3[4] = {'P', 's', 'i', (char)NULL};
    char sentence_4[4] = {"Psi"};
    printf("sentence_1 : %s \n", sentence_1); // %s 를 통해서 NULL값 나올 때 까지 문자열을 출력.
    printf("sentence_2 : %s \n", sentence_2);
    printf("sentence_3 : %s \n", sentence_3);
    printf("sentence_4 : %s \n", sentence_4);
    return 0;
}

/*
sentence_1 : Psi 
sentence_2 : Psi 
sentence_3 : Psi 
sentence_4 : Psi 
"Psi" 로 정의해놓고 배열의 크기를 3 으로 잡으면
sentence에는 끝에 NULL 이 들어가지 않으므로 sentence의 문자열을 출력하라고 했을 때
NULL 이 언제 나올지 모르기 때문에 혀용되지 않는 메모리 범위를 읽게되는 문제가 발생
*/