#include <stdio.h>

int main() {
	long a, b; //long은 byte 64, int는 byte 32
    scanf("%li %li", &a, &b);
	
    printf("%li\n",a+b); // long이니까 %d 대신 %li
    printf("%li\n",a-b);
    printf("%li\n",a*b);
    printf("%li\n",a/b);
    printf("%li\n",a%b);

	return 0;
}