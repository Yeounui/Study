#include <stdio.h>

int main() {
	long a, b, c;
    scanf("%li %li %li", &a, &b, &c);

    printf("%li\n", ((a+b)%c)); // 13%4 >> 1
    printf("%li\n", ((a%c)+(b%c))%c); // 5 + 0 % 4 >> 1
    printf("%li\n", (a*b)%c); // 40 % 4 >> 0
    printf("%li\n", ((a%c) * (b%c))%c); // (1 * 0) % 4 >> 0

	return 0;
}