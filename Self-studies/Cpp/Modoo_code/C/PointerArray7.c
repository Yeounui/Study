int main() {
    int arr[2][3] = {{1, 2, 3}, {4, 5, 6}};
    printf("전체 크기 : %d \n", sizeof(arr));
    printf("총 열의 개수 : %d \n", sizeof(arr[0]) / sizeof(arr[0][0]));
    printf("총 행의 개수 : %d \n", sizeof(arr) / sizeof(arr[0]));
}

/*
전체 크기 : 24 = 6 * 4 (int)
총 열의 개수 : 3 = (3 * 4) / (1 * 4)
총 행의 개수 : 2 = 24 / (3 * 4)
*/