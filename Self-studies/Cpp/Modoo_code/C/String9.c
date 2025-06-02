/* 문자열
프로그램이 실행되서 메모리에 로드되면, 5 가지 종류의 영역 (text segment, data segment, bss segment, heap, stack) 이 존재.
이 때, 텍스트 세그먼트(text segment) 에 프로그램 코드와 상수, 리터럴 등이 여기서 정의됩니다. 텍스트 세그먼트에 있는 내용들은 읽기만 가능.
*/
#include <stdio.h>

int main() {
    char str[] = "hello"; // str array에 {'h', 'e', 'l', 'l', 'o', '\0'} 다음과 같이 문자열 복사. Stack이라는 메모리 수정이 가능한 영역에 정의.
    char *pstr = "goodbye"; //string literal: literal은 소스코드(Text segment) 상에 포함되어 고정되어있어 못 바꿈.

    str[1] = 'a';
    // pstr[1] = 'a';

    return 0;
}

/*if (str1 == str2) string은 주소값임. 0번 째 자리의 주소값부터 문자열따라 값 메모리에 배열. 따라서 str1 == str2는 주소값이 같은 지 비교.*/
/*if (str1 == "abc") "abc"는 literal. 따라서 "abc"와 str1의 주소값이 같은지 비교. */
/*str1 = str2 str1은 string literal이라 못 바꿈*/
/*문자열 바꾸는 데 제약이 많음, 따라서 보조하는 함수가 필요.
1. 문자열 내의 총 문자의 수를 세는 함수
2. 문자열을 복사하는 함수
3. 문자열을 합치는 함수
4. 문자열을 비교하는 함수*/