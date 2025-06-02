#include <iostream>
namespace { // 이름 없는 namespace
    // 이 함수는 이 파일 안에서만 사용 가능.
    // = static int OnlyInThisFile()
    int OnlyInThisFile() {
        std::cout << "hi" << std::endl
        << "my name is "
        << "Psi" << std::endl;
        return 0;
    }
    // 이 변수 역시 static int x 와 동일합니다.
    int only_in_this_file = 0;
}

int main() {
    OnlyInThisFile();
    only_in_this_file = 3;
}