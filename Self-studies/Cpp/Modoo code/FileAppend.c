/* fopen 의 'append' 기능 사용*/
#include <stdio.h>
int main() {
    FILE *fp = fopen("some_data.txt", "a");
    char c;
    if (fp == NULL) {
        printf("파일 열기를 실패하였습니다! \n");
        return 0;
    }
    /* 아래 내용이 파일 뒤에 덧붙여진다.*/
    fputs("IS ADDED HAHAHAHA", fp);
    fclose(fp);
}
