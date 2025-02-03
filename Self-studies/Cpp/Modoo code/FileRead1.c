/* fgets 로 a.txt 에서 내용을 입력 받는다. */
#include <stdio.h>

int main() {
    FILE *fp = fopen("FileWrite.txt", "r");
    char buf[20]; // 내용을 입력받을 곳

    if (fp == NULL) {
        printf("READ ERROR !! \n");
        return 0;
    }

    fgets(buf, 20, fp);
    printf("입력받는 내용 : %s \n", buf);
    fclose(fp);
    return 0;
}