#include <iostream>

void print(int x) { std::cout << "int : " << x << std::endl; }
void print(char x) { std::cout << "char : " << x << std::endl; }
void print(double x) { std::cout << "double : " << x << std::endl; }
// 같은 이름의 함수가 여러 개 => 오버로딩. 컴파일러는 인자를 통해 이 함수들을 구별 (우선 순위는 순서대로).
// 1. type이 같은 함수
// 2. 정확히 일치하는 type이 없는 경우 아래와 같은 형변환을 통해서 일치하는 함수
//      char, unsigned char, short => int
//      unsigned short => 크기에 따라 int 혹은 unsigned int
//      float => double
//      enum => int
// 3. 좀더 포괄적인 형변환을 통해 일치하는 함수.
//      임의의 numeric type => 다른 numeric type으로 변환. (ex) float -> int)
//      enum => 임의의 numeric type으로 변환. (ex) enum -> double)
//      pointer type 혹은 numeric type 0 => pointer type이나 numeric type으로 변환
//      pointer => void pointer
// 4. 유저 정의된 type 변환으로 일치하는 것 ()
// 5. 오류로 판단.

int main() {
    int a = 1;
    char b = 'c';
    double c = 3.2f; // print(double x) 가 없을 시, 임의의 numeric type => 다른 numeric type으로 변환
    // => int 인자 함수와 char 인자 함수 둘 모두 우선 순위가 같기에 오류가 남.

    print(a);
    print(b);
    print(c);
    
    return 0;
}
