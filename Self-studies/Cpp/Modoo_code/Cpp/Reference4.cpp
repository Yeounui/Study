#include <iostream>
int main() {
    int arr[3] = {1, 2, 3};
    int(&ref)[3] = arr; // 배열에 대한 레퍼런스 불가. (불가: &ref[3]); 배열 자체에 대한 레퍼런스만 가능.
    ref[0] = 2;
    ref[1] = 3;
    ref[2] = 1;
    std::cout << arr[0] << arr[1] << arr[2] << std::endl;
    return 0;
}
