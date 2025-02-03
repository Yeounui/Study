/* fscanf 이용하기 */
#include <stdio.h>

int main() {
    FILE *fp = fopen("some_data.txt", "r");
    char data[100];

    if (fp == NULL) {
        printf("파일 열기 오류! \n");
        return 0;
    }

    printf("---- 입력 받은 단어들 ---- \n");
    while (fscanf(fp, "%s", data) != EOF) { //fscanf: 개행마다 가져옴. 단어 별로 얻음.
        printf("%s \n", data);
    }

    fclose(fp);
}
