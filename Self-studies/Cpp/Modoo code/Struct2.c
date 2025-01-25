/* 구조체 예제*/
#include <stdio.h>

struct Books {
    /* 책 이름 */
    char name[30];
    /* 저자 이름 */
    char auth[30];
    /* 출판사 이름 */
    char publ[30];
    /* 빌려 졌나요? */
    int borrowed; //구조체에선 정의 불가 eg) int borrowed = 1;
};

int main() {
    struct Books book_list[3];
    int i;
    
    for (i = 0; i < 3; i++) {
        printf("책 %d 정보 입력 : ", i);
        scanf("%s%s%s", book_list[i].name, book_list[i].auth, book_list[i].publ); // string1, string2, string3 = name, author, publ
        book_list[i].borrowed = 0;
    }

    for (i = 0; i < 3; i++) {
        printf("------------------------------- \n");
        printf("책 %s 의 정보\n", book_list[i].name);
        printf("저자 : %s \n", book_list[i].auth);
        printf("출판사 : %s \n", book_list[i].publ);
        
        if (book_list[i].borrowed == 0) {
            printf("안 빌려짐\n");
        } else {
            printf("빌려짐 \n");
        }
    }
    
    return 0;
}
