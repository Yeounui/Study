#include <stdio.h>
int main() {
    /* 현재 fp 에 abcdef 가 들어있는 상태*/
    FILE *fp = fopen("FileWrite.txt", "r");
    fgetc(fp); //a
    fgetc(fp); //b
    fgetc(fp); //c
    fgetc(fp); //d

    /* d 까지 입력받았으니 파일 위치지정자는 이제 e 를 가리키고 있다 */
    fseek(fp, 0, SEEK_SET); // fseek(str, pos, macro_const) #SEEK_SET: 파일의 처음. #SEEK_CUR: 현재의 위치. #SEEK_END: 파일의 맨 마지막.
    printf("다시 파일 처음에서 입력 받는다면 : %c \n", fgetc(fp));
    fclose(fp);
    return 0;
}