#include <stdio.h>

struct TEST {
    int age;
    int gender;
    char name[20];
};
int set_human(struct TEST *a, int age, int gender, const char *name);
char copy_str(char *dest, const char *src);
int main() {
    struct TEST human;
    
    set_human(&human, 10, 1, "Lee");

    printf("AGE : %d // Gender : %d // Name : %s \n", human.age, human.gender, human.name);
    return 0;
}
int set_human(struct TEST *a, int age, int gender, const char *name) { // 구조체는 포인터 값으로 전달해야함.
    a->age = age;
    a->gender = gender;
    copy_str(a->name, name);

    return 0;
}
char copy_str(char *dest, const char *src) { // 리터럴은은 char* 가 가리킬 수 없음. const char로 받았다면 하위 명령도 const char로 받아야. String9.c 참조.
    while (*src) {
        *dest = *src;
        src++;
        dest++;
    }

    *dest = '\0';

    return 1;
}