/* 열거형의 도입 */
#include <stdio.h>
enum { RED = 3, BLUE, WHITE, BLACK }; // python list와 같음. 자릿수도 0부터. 그러나 추가로 RED = 3 정의하면 따로 정의되기 전까지 다음 자리가 1씩 늘어남.
int main() {
    int palette = BLACK;
    printf("%d \n", palette);
    switch (palette) {
        case RED:
            printf("palette : RED \n");
            break;
        case BLUE:
            printf("palette : BLUE \n");
            break;
        case WHITE:
            printf("palette : WHITE \n");
            break;
        case BLACK:
            printf("palette : BLACK \n");
            break;
    }
}
