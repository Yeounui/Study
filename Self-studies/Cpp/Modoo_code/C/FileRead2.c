/* 한 글자씩 입력받기*/
#include <stdio.h>

int main() {
    FILE *fp = fopen("FileWrite.txt", "r");
    char c;

    while ((c = fgetc(fp)) != EOF) {
        printf("%c", c);
    }

    fclose(fp);
    return 0;
}