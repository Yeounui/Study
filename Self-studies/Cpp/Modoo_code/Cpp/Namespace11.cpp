#include "header1.h"
#include "header2.h"

using namespace header1;
int main() {
foo(); // header1 에 있는 함수를 호출
header2::foo(); // header2 에 있는 함수를 호출
bar(); // header1 에 있는 함수를 호출
header2::bar(); // header2 에 있는 함수를 호출
}

// g++ Namespace1.cpp foo.cpp -fdiagnostics-color=always -g -o ./Namespace1 -I "./Study/Self-studies/Cpp/Modoo_code/Cpp/include/"