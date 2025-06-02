#include <iostream>

int main() {
    int* p = new int; // C의 malloc과 대응; 메모리의 Heap에 int 크기를 할당하고, 그 메모리 주소값을 p에 정의.
    *p = 10;
    std::cout << *p << std::endl;
    delete p; // C의 free와 대응; New를 통해 할당된 메모리 공간만 delete가 해제 가능
    // New로 정의되지 않은 다른 변수를 해제하려 하면 에러
    return 0;
}