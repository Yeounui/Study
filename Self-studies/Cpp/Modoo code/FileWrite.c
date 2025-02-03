/* a.txt 에 내용을 기록한다. */
#include <stdio.h>
int main() {
    FILE *fp;
    fp = fopen("FileWrite.txt", "w");

    if (fp == NULL) {
        printf("Write Error!!\n");
        return 0;
    }

    fputs("Hello World!!! \n", fp);
    fclose(fp);
    return 0;
}