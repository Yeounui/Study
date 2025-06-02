/* new 로 배열 할당하기 */

#include <iostream>
int main() {
    int arr_size;

    std::cout << "array size : ";
    std::cin >> arr_size;

    int *list = new int[arr_size]; // C는 변수의 선언을 모두 최상단에 몰아서 해야하지만 C++ 은 그렇지 않아도 됨.
    for (int i = 0; i < arr_size; i++) {
        std::cin >> list[i];
    }
    for (int i = 0; i < arr_size; i++) {
        std::cout << i << "th element of list : " << list[i] << std::endl;
    }
    delete[] list; // new type[]이면 delete[]으로 해제.
    
    return 0;
}
/*
array size : 5
9
6
0
6
2

0th element of list : 9
1th element of list : 6
2th element of list : 0
3th element of list : 6
4th element of list : 2
*/