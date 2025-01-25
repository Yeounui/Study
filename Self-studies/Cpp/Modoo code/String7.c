/* 이상한 scanf */
#include <stdio.h>

int main() {
    int num;
    char c; // char str[30]
    printf("숫자를 입력하세요 : "); // 공백 문자(' ', '\n', '\t')를 받으면 scanf는 더 이상 입력을 안 받음. 첫 번째 scanf에서 "1\n"을 넣으면 1만 가져가고 "\n"은 버퍼에 남겨둠.
    scanf("%d", &num);
    printf("문자를 입력하세요 : "); // c는 한 글자만 가져가므로 남은 '\n'을 바로 가져가기에 두 번째 input 안 받음. %s는 됨.
    scanf("%c", &c);
    return 0;
}